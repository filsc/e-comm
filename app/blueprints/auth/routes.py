from app import app
from flask import redirect, render_template, flash, request, url_for
from flask_login import login_user
from app.models import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is None or not user.check_password(request.form.get('password')):
            flash('Either that user does not exist or the password is incorrect. Try again.', 'warning')
            return redirect(url_for('login'))
        remember_me = True if request.form.get('rememberme') is not None else False
        login_user(user, remember=request.form.get('rememberme'))
        print('SUCCESS')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User()
        u.from_dict(request.form)
        u.save()
        flash('User created successfully', 'info')
        return redirect(url_for('app.login'))
    return render_template('register.html')