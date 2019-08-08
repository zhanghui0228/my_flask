from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')
@app.route('/hello/<name>')
def hello(name):
	return render_template("hello.html", name = name)

@app.route('/hello/<score>')
def hello_name(score):
	return render_template('hello.html', marks = score)

@app.route('/result')
def result():
	dict = {'pyh':50, 'che':70, 'maths':70}
	return render_template('result.html', result = dict)
if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug = True)
