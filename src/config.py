class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://localhost/todo_api_prod'


class DevelopmentConfig(Config):
    DATABASE_URI = 'postgresql://localhost/todo_api'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
