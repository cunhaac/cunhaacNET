from database.models import Users, Roles, db

username = input('Username to be Admin: ')


user = Users.query.filter_by(username=username).first()
token = user.get_reset_token()
user = Users.verify_reset_token(token)

super_role = ('1', 'Administrator', '1')
user.roles = list(super_role)
db.session.commit()
