# #!/usr/bin/env python3

from flask_login import LoginManager, login_user, current_user

from app import app
from database.models import Users

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))
