# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for, escape, request
app = Flask(__name__)
app.secret_key = 'zhanghuitest'

@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		return 'Logged in as: ' + username + '<br>' +\
			"<b><a href = '/logout'>click here to log out</a></b>"
	return "你暂未登陆<br><a href = '/login'></b>" +\
		"点这里登陆</b></a>"

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
	<form action = "" method = "post">
		<p><input type = text name = "username"/></p>
		<p><input type = submit value = "登录"/></p>
	</form>
	'''

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
