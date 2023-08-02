from ..models.user_model import User

import datetime
import jwt
from flask import current_app


class AuthService:
    @staticmethod
    def generate_secure_token(user_id):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'user_id': user_id
            }
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token

    @staticmethod
    def decode_secure_token(token):
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def authenticate_user(email, password):
        user = User.find_by_email(email)
        if user and user.check_password(password):
            return user



