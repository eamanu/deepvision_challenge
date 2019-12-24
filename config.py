import os

version = open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'version'))

class Config(object):
    VERSION = version.read().strip()
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/openapi'
    DEBUG = True
    pass


class DevConfig(Config):
    DEBUG = True
    pass


class ProdConfig(Config):
    pass

