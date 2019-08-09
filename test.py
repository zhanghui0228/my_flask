from flask import Flask, url_for, render_template, redirect, request
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def index(name):
	return render_template('hello.html', name = name)



if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
