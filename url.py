from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
	return "hello ADMIN"

@app.route('/admin/<zhh>')
def hello_guest(zhh):
	return 'hellow %s as Guest' % zhh

@app.route('/user/<name>')
def hello_user(name):
	if name == "admin":
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', zhh = name))

if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
