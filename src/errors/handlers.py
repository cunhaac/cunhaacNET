#!/usr/bin/env python3

from flask import render_template
from app import app

@app.route('/403', methods=(['GET'])
def error_403(error):
	return render_template('/includes/_403.html'), 403

@app.route('/404', methods=(['GET'])
def error_404(error):
	return render_template('/includes/_404.html'), 404

@app.route('/500', methods=(['GET'])
def error_500(error):
	return render_template('/includes/_500.html'), 500