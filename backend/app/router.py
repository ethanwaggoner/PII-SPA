from flask_restx import Api
from flask_limiter.errors import RateLimitExceeded

from .resources.auth_resource import LoginResource, LogoutResource


api = Api(
    version='1.0',
    title='PII',
    description='Backend API for PII project',
)


auth_ns = api.namespace('auth', description='Authentication related operations')
deauth_ns = api.namespace('deauth', description='Logout related operations')

auth_ns.add_resource(LoginResource, '/')
deauth_ns.add_resource(LogoutResource, '/')


@api.errorhandler(RateLimitExceeded)
def rate_limit_handler(e):
    return {'message': 'Too many logins :)'}, 429



