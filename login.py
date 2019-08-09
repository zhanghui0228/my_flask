from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def index():
	return render_template('login.html')

@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['name']
		return redirect(url_for('success', name = user))
	else:
		user = request.args.get('name')
		return redirect(url_for('success', name = user))

if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
