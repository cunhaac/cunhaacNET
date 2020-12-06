#!/usr/bin/env python3

import requests
from urllib.request import urlopen

from flask import render_template, redirect
from flask_user import roles_required
import users.helpers.manager_login as manager

from app import app


@app.route('/dashboard', methods=['GET', 'POST'])
def cunhaac_dashboard():

    if not manager.current_user.is_authenticated:
        return redirect('/login')

    public_ipv4 = urlopen('https://api.ipify.org').read().decode('utf8')
    public_ipv6 = urlopen('https://api64.ipify.org').read().decode('utf8')
    
    if len(public_ipv6) < 15:
        public_ipv6 = "unavailable"

    response = requests.get('https://api.myip.com')
    cc = response.json()['cc']

    ###FIXME request flag from api, learn json struggles, go go go     
    flag_ = requests.get('http://api.ipstack.com/' + public_ipv4 + '?access_key=7eadd30a1c0ad475ad2fae3afe4d8e73&format=1')
    flag = flag_.json()['location']['country_flag']

    return render_template('dashboard.html',
                           public_ipv4=public_ipv4,
                           cc=flag,
                           public_ipv6=public_ipv6)


@app.route('/dashboard/admin', methods=(['GET', 'POST']))
@roles_required('Administrator')
def admin():
    return 'Pedro Cunha'
