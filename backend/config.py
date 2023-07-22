import os
from dotenv import load_dotenv


class Config(object):

    load_dotenv()

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.getenv('SECRET_KEY')

    OAUTHLIB_RELAX_TOKEN_SCOPE = True

    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_ENGINE'),
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_PORT'),
        os.getenv('DB_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_CONFIRMABLE = True

    JWT_SECRET_KEY = os.getenv('SECRET_KEY')

    GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')


class ProductionConfig(Config):
    DEBUG = False

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    OAUTHLIB_INSECURE_TRANSPORT = False


class DebugConfig(Config):
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True

    OAUTHLIB_INSECURE_TRANSPORT = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
