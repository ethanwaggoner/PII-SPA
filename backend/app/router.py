from flask_restx import Api
from .resources.auth_resource import LoginResource


api = Api(
    version='1.0',
    title='PII',
    description='Backend API for PII project',
)


auth_ns = api.namespace('auth', description='Authentication related operations')

auth_ns.add_resource(LoginResource, '/')



