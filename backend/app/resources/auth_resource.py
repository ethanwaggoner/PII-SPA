from flask_restx import Resource, abort, reqparse
from werkzeug.exceptions import Unauthorized
from ..services.auth_service import AuthService
from ..limiter import limiter


class LoginResource(Resource):
    decorators = [limiter.limit("5/minute")]

    def post(self):
        parser = reqparse.RequestParser()

        try:
            parser.add_argument('email', type=str, required=True)
            parser.add_argument('password', type=str, required=True)
            args = parser.parse_args()
            email = args['email']
            password = args['password']
            auth_service = AuthService()
            user = auth_service.authenticate_user(email, password)
            if user is None:
                abort(401, message="Authentication failed.")
            token = auth_service.generate_secure_token(user.fs_uniquifier)
            return {
                'success': True,
                'token': token,
                'user_id': user.fs_uniquifier,
                'is_authenticated': True,
            }, 200
        except Exception:
            abort(401, message="Authentication failed.")


class LogoutResource(Resource):
    decorators = [limiter.limit("5/minute")]

    def post(self):
        parser = reqparse.RequestParser()

        try:
            parser.add_argument('token', type=str, required=True)
            args = parser.parse_args()
            token = args['token']

            auth_service = AuthService()
            fs_uniquifier = auth_service.decode_secure_token(token)
            if auth_service.logout_user(fs_uniquifier):
                return {'success': True}, 200
            else:
                return {'success': False}, 401
        except Unauthorized:
            abort(401, message="Authentication failed.")


