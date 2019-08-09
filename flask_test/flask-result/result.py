# -*- coding: utf-8 -*-
import commands
from flask import Flask, render_template
app = Flask(__name__)

USED = commands.getoutput("free -m|grep Mem|awk '{print $3}'")
Free = commands.getoutput("free -m|grep Mem|awk '{print $4}'")
Total = commands.getoutput("free -m|grep Mem|awk '{print $2}'")


@app.route('/result')
def result():
	dict = {'Mem_used':USED,'Mem_free':Free,'Mem_total':Total}
	#dict = {'phy':'88', 'cache':40, 'maths':60}
	return render_template('result.html', result = dict)

if __name__ == '__main__':
	app.run('0.0.0.0', '8090', debug =True)
