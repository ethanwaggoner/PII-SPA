from flask import jsonify, request
from flask_restx import Resource, abort, reqparse
from werkzeug.exceptions import Unauthorized


class LoginResource(Resource):
    def __init__(self, auth_service):
        super(LoginResource, self).__init__()
        self.auth_service = auth_service

    def post(self):
        if not request.is_json:
            abort(400, message="Invalid request.")

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        try:
            user = self.auth_service.authenticate_user(email, password)
            token = self.auth_service.generate_secure_token(user.id)
            return {
                'success': True,
                'token': token,
                'user': user.to_dict()
            }, 200
        except Unauthorized:
            abort(401, message="Authentication failed.")





