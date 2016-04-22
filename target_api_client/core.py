import requests
from requests.auth import HTTPBasicAuth
from .errors import *
from .config import config as target_config


class TargetApiClient(object):
    def __init__(self, account_sid, access_token):
        self.config = target_config
        self.set_config({
            'account_sid': account_sid,
            'access_token': access_token
        })

    def set_config(self, config):
        self.config.update(config)

    def call(self, resource, params):
        if 'account_sid' not in self.config:
            raise TargetApiParameterNotImplementedError(parameter='account_sid')

        if 'access_token' not in self.config:
            raise TargetApiParameterNotImplementedError(parameter='access_token')

        if not self._validate_parameters(params):
            raise TargetApiParamsError()

        response = self._make_call(resource, params)

        if response.status_code != 200:
            # Process errors
            if response.status_code == 400:
                raise TargetApiBadRequestError()
            elif response.status_code == 401:
                raise TargetApiUnauthorizedError()
            elif response.status_code == 404:
                raise TargetApiNotFoundError()
            elif response.status_code == 405:
                raise TargetApiMethodNotAllowedError()
            elif response.status_code == 500:
                raise TargetApiServerError()
            elif response.status_code == 503:
                raise TargetApiServiceUnavailableError()
            else:
                raise TargetApiUnknownError()

        if response.headers['content-type'].find('application/json') != -1:
            return response.json()

        return response.content

    def _make_call(self, resource, params):
        return requests.get(
            self._generate_url(resource),
            params=params,
            auth=HTTPBasicAuth(self.config['account_sid'], self.config['access_token'])
        )

    @classmethod
    def _validate_parameters(cls, params):
        if 'Query' not in params:
            return False

        return True

    def _generate_url(self, resource_name):
        if 'base_url' not in self.config:
            raise TargetApiParameterNotImplementedError(parameter='base_url')

        if 'account_sid' not in self.config:
            raise TargetApiParameterNotImplementedError(parameter='account_sid')

        return self.config['base_url']\
            .replace('{AccountSID}', self.config['account_sid'])\
            .replace('{ResourceName}', resource_name)
