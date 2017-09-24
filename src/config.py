class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/todo_api_prod'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/todo_api'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
