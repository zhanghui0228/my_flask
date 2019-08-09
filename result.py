from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
	dict = {'phy':'88', 'cache':40, 'maths':60}
	return render_template('result.html', result = dict)

if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug =True)
