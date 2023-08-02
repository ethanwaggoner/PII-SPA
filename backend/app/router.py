from flask_restx import Api
from .services.auth_service import AuthService
from .resources.auth_resource import LoginResource


api = Api(
    version='1.0',
    title='PII',
    description='Backend API for PII project',
)


auth_resource = AuthService()

auth_ns = api.namespace('login')

auth_ns.add_resource(LoginResource, path='/', auth_service=auth_resource)



