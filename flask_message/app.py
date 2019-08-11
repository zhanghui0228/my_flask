from flask import Flask, flash, render_template, request, redirect, url_for
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
	error = None
	print (request.method)
	if request.method == 'POST':
		if request.form['username'] != 'admin' or  request.form['password'] != 'admin':
			error = 'Invalid username or password. Please try again!'
		else:
			flash('You were successfully logged in')
			return redirect(url_for('index'))
	return render_template('login.html', error = error)



if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
