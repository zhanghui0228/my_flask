from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	#return redirect(url_for('login'))
	return render_template('log_in.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.mothod == 'POST':
		if request.form['username'] == 'admin':
			return redirect(url_for('success'))
		else:
			abort(401)

@app.route('/success')
def success():
	return 'logged in successfully'

if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
