from app import app
from flask import render_template, redirect
from .forms import LoginForm

@app.route('/login', mothods = ['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Miguel' }
	posts = [
		{
			'author': { 'nickname': 'John' },
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': { 'nickname': 'Susan' },
			'body': 'the Avengeers novie was so cool!'
		}
	]
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts)
