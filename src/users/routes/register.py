#!/usr/bin/env python3

import re

from flask import render_template, redirect, request, url_for

from app import app, db
from database.models import Users, generate_password_hash
import users.helpers.manager_login as manager

from dashboard.routes.dashboard import cunhaac_dashboard


def valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return True if (re.search(regex, email)) else False


def valid_password(password, confirm_password):
    return True if password == confirm_password else False


def valid_username(username):
    return True if Users.query.filter_by(username=username).first() is None else False


def min_chars(password):
    return True if len(password) > 7 else False


@app.route('/register', methods=['POST', 'GET'])
def cunhaac_register():
    register_error = None

    if manager.current_user.is_authenticated:
        return redirect(url_for('cunhaac_dashboard'))

    if request.method == 'POST':
        name             = request.form['name']
        username         = request.form['username']
        password         = request.form['password']
        confirm_password = request.form['confirm_password']
        email            = request.form['email']

        if valid_username(username) is False:
            register_error = 'Username already taken!'
        if min_chars(password) is False:
            register_error = 'Password minimum of 8 chars!'
        if valid_email(email) is False:
            register_error = 'Invalid email!'
        if valid_password(password, confirm_password) is False:
            register_error = 'Passwords do not match!'

        new_user = Users(name=name,
                         username=username,
                         secure_password=generate_password_hash(password),
                         email=email)

        if (valid_username(username)
           and min_chars(password)
           and valid_email(email)
           and valid_password(password, confirm_password)
           is True):
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return str(e)

    return render_template('cunhaac_register.html',
                           register_error=register_error)
