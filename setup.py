try:
    import multiprocessing
except ImportError:
    pass


from setuptools import setup

setup(
    name='target-api-client',
    version='1.0',
    description='Target.com API Client',
    url='https://github.com/kronas/python-target-api-client',
        
    author='Kronas',
    author_email='kronas.sw@gmail.com',
    license='MIT',

    packages=['target_api_client'],

    install_requires=[
        'requests>=2.9.1'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    zip_safe=False,
)
