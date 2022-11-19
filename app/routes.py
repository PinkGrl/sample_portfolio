from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/AboutMe')
def AboutMe():
    """Description URL"""
    return render_template('AboutMe.html', title='About Me!')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login in as {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
