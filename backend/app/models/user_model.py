import uuid
import hashlib
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore
from sqlalchemy import bindparam

from .database import db


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    fs_uniquifier = db.Column(db.String(255), default=uuid.uuid4, unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_authenticated = db.Column(db.Boolean(), default=False, nullable=False)
    last_login_at = db.Column(db.DateTime(), nullable=True)
    current_login_at = db.Column(db.DateTime(), nullable=True)
    last_login_ip = db.Column(db.String(255), nullable=True)
    current_login_ip = db.Column(db.String(255), nullable=True)
    login_count = db.Column(db.Integer(), nullable=False, default=0)

    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email.split('@')[0]

    def to_dict(self):
        return {
            'id': self.id,
            'fs_uniquifier': self.fs_uniquifier,
            'email': self.email,
            'is_authenticated': self.is_authenticated,
            'last_login_at': self.last_login_at,
            'current_login_at': self.current_login_at,
            'last_login_ip': self.last_login_ip,
            'current_login_ip': self.current_login_ip,
            'login_count': self.login_count,
            'roles': [role.name for role in self.roles]
        }

    @classmethod
    def add_user(cls, email, password):
        email_hash = hashlib.sha256(email.encode('utf-8')).hexdigest()
        user = cls(email_hash, password)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def find_by_email(cls, email):
        email_hash = hashlib.sha256(email.encode('utf-8')).hexdigest()
        query = db.select(cls).where(cls.email == bindparam('email_hash'))
        return db.session.execute(query, {'email_hash': email_hash}).first()

    @classmethod
    def email_exists(cls, email) -> bool:
        email_hash = hashlib.sha256(email.encode('utf-8')).hexdigest()
        query = db.select(cls.email).where(cls.email == bindparam('email_hash'))
        return db.session.execute(query, {'email_hash': email_hash}) is not None


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)
