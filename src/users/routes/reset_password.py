#!/usr/bin/env python3

from flask import render_template, redirect, request, url_for
from flask_mail import Message

from app import app, db, mail
from users.routes.register import valid_email, valid_password, min_chars
from users.routes.login import cunhaac_login
from database.models import Users, generate_password_hash


def send_reset_email(true_email):
	token = true_email.get_reset_token()
	msg = Message('Password Reset Request - cunhaacNET',
                  sender='testing_your_ass@sapo.pt',
                  recipients=[email])

	msg.body = f''' To reset your password, visit the following link:
	            {url_for('reset_password', token=token, _external=True)}
				If you did not make this request then simply ignore this message.
			    '''
	try:
		mail.send(msg)
	except Exception as e:
		return str(e)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_request():
	request_error = None

	if request.method == 'POST':
		global email
		email = request.form['email']
		true_email = Users.query.filter_by(email=email).first()
		if true_email is None:
			request_error = 'Email do not exist!'
		elif valid_email(email) is False:
			request_error = 'Invalid email!'
		else:
			send_reset_email(true_email)
			request_error = 'An email has been sent with instructions!'

	return render_template('reset_password_request.html', request_error=request_error)


@app.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_password(token):
	reset_error = None

	user = Users.verify_reset_token(token)
	
	if user is None:
		reset_error = 'This is an invalid or expired token!'

	if request.method == 'POST':
		password = request.form['password']
		confirm_password = request.form['confirm_password']
		
		changed_password = generate_password_hash(password)

		if valid_password(password, confirm_password) is False:
			reset_error = 'Passwords do not match!'
		elif min_chars(password) is False:
			reset_error = 'Password minimum of 8 chars!'
		else:
			try:
				user.secure_password = changed_password
				db.session.commit()
				return redirect('/')
			except Exception as e:
				# FIXME RETURN THE EXCEPTION IN BLANK PAGE, PROBABLY SOME 403 ERROR HERE
				return str(e)
	return render_template('reset_password.html', reset_error=reset_error)
