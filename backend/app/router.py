from flask_restx import API


api = API(
    title='PII',
    description='Backend API for PII project'
)

overview_ns = api.namespace('overview', description='Overview Operations')


