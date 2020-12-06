#!/usr/bin/env python3

class Authentication():

    from database.models import Users

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user(self):
        user = self.Users.query.filter_by(username=self.username).first()
        return user
    
    def validate(self):
        username = self.Users.query.filter_by(username=self.username).first()
        return False if username is None or not username.check_password(password=self.password) else True
    
