from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/hello/<name>')
def hello(name):
	return render_template("hello.html", name = name)

if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
