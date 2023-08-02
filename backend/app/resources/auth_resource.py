from flask_restx import Resource, abort, reqparse
from werkzeug.exceptions import Unauthorized
from ..services.auth_service import AuthService


class LoginResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        try:
            auth_service = AuthService()
            user = auth_service.authenticate_user(email, password)
            token = auth_service.generate_secure_token(user.id)
            return {
                'success': True,
                'token': token,
                'user': user.to_dict()
            }, 200
        except Unauthorized:
            abort(401, message="Authentication failed.")




