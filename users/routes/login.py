#!/usr/bin/env python3

from flask import render_template, redirect, request, url_for

import users.helpers.authentication as auth
import users.helpers.manager_login as manager

from app import app
from users.routes.register import cunhaac_register
from dashboard.routes.dashboard import cunhaac_dashboard
from users.helpers.manager_login import load_user


@app.route('/login', methods=['GET', 'POST'])
def cunhaac_login():

    login_error = None

    if manager.current_user.is_authenticated:
        return redirect(url_for('cunhaac_dashboard'))

    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        user = auth.Authentication(username, password)
        _user = user.get_user()
        
        if user.validate() is True:
            manager.login_user(_user)
            return redirect(url_for('cunhaac_dashboard'))
        else:
            login_error = 'Invalid Credentials. Please try again.'

    return render_template('cunhaac_login.html', login_error=login_error)
