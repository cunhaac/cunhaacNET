#!/usr/bin/env python3

from flask import redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user

from users.routes.login import cunhaac_login
from dashboard.routes.dashboard import cunhaac_dashboard
from database.models import Users
from app import app

import users.routes.register
import users.routes.reset_password


@app.route('/', methods=['GET'])
def main():
    if current_user.is_authenticated:
        return redirect(url_for('cunhaac_dashboard'))
    else:
        return redirect(url_for('cunhaac_login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
