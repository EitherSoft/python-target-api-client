__all__ = [
    'TargetApiError',
    'TargetApiParamsError',
    'TargetApiBadRequestError',
    'TargetApiUnauthorizedError',
    'TargetApiNotFoundError',
    'TargetApiMethodNotAllowedError',
    'TargetApiServerError',
    'TargetApiServiceUnavailableError',
    'TargetApiParameterNotImplementedError',
    'TargetApiUnknownError'
]


class TargetApiError(Exception):
    """
        Errors from Target API client
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiError, self).__init__()
        self.args = args
        self.code = kwargs.pop('code', None)
        self.msg = kwargs.pop('msg', None)

    def __str__(self):  # pragma: no cover
        if self.code is not None or self.msg is not None:
            return 'TargetAPI error: %(msg)s (%(code)s)' % self.__dict__
        return Exception.__str__(self)


class TargetApiParamsError(TargetApiError):
    """
        Error, when validate of request parameters is False
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiParamsError, self).__init__()
        self.msg = kwargs.pop('msg', 'Invalid parameters')

    def __str__(self):
        return 'TargetAPI error: %(msg)s' % self.__dict__


class TargetApiBadRequestError(TargetApiError):
    """
        Server return 400 code - Bad request
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiBadRequestError, self).__init__()
        self.code = kwargs.pop('code', 400)
        self.msg = kwargs.pop('msg', 'Bad request')


class TargetApiUnauthorizedError(TargetApiError):
    """
        Server return 401 code - Unauthorized (Bad credentials)
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiUnauthorizedError, self).__init__()
        self.code = kwargs.pop('code', 401)
        self.msg = kwargs.pop('msg', 'Unauthorized')


class TargetApiNotFoundError(TargetApiError):
    """
        Server return 404 code - Not found
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiNotFoundError, self).__init__()
        self.code = kwargs.pop('code', 404)
        self.msg = kwargs.pop('msg', 'Not found')


class TargetApiMethodNotAllowedError(TargetApiError):
    """
        Server return 405 code - Method not allowed
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiMethodNotAllowedError, self).__init__()
        self.code = kwargs.pop('code', 405)
        self.msg = kwargs.pop('msg', 'Method not allowed')


class TargetApiServerError(TargetApiError):
    """
        Server return 500 code - Internal server error
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiServerError, self).__init__()
        self.code = kwargs.pop('code', 500)
        self.msg = kwargs.pop('msg', 'Internal server error')


class TargetApiServiceUnavailableError(TargetApiError):
    """
        Server return 503 code - Service is unavailable
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiServiceUnavailableError, self).__init__()
        self.code = kwargs.pop('code', 503)
        self.msg = kwargs.pop('msg', 'Service unavailable')


class TargetApiParameterNotImplementedError(TargetApiError):
    """
        Error, when some required parameter is not implemented
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiParameterNotImplementedError, self).__init__()
        self.parameter = kwargs.pop('parameter', '')

    def __str__(self):
        if self.parameter is not None:
            return 'TargetAPI error: Parameter %(parameter)s not implemented' % self.__dict__
        return 'TargetAPI error: Parameter not implemented'


class TargetApiUnknownError(TargetApiError):
    """
        Unknown error
    """
    def __init__(self, *args, **kwargs):
        super(TargetApiUnknownError, self).__init__()
        self.msg = kwargs.pop('msg', 'Unknown error')
