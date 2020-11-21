# !/usr/bin/env python3

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from database.helpers import secrets
from app import db


class Users(db.Model, UserMixin):
    '''UserMixin has 4 diferent functions such as is_active, is_authenticated,
    is_anonymous and get_id, the 3 firsts funcions return Boolean and the last
    one get the id of the user...'''
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    secure_password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    roles = db.relationship('Roles', secondary='User_Roles')

    def __repr__(self):
        return f'{self.id}, {self.username}, {self.name}, {self.email}'

    def set_password(self, password):
        self.secure_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.secure_password, password)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(secrets.SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(secrets.SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except Exception:
            return None
        return Users.query.get(user_id)


class Roles(db.Model):
    __tablename__ = 'Roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'Role {self.name}'


class UserRoles(db.Model):
    __tablename__ = 'User_Roles'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('Users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('Roles.id', ondelete='CASCADE'))
    

