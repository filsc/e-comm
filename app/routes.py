from flask import current_app as app, render_template
from app.models import Post, User
from flask_login import login_user, logout_user, current_user

#@app.route('/')
def home():
    context = dict()
    return render_template('app/templates/index.html')

@app.route('/contact')
def shop(): 
    return 'something'

@app.route('/contact')
def contact(): 
    return 'something'

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully.', 'warning')
    return redirect(url_for('login'))

@auth route('/login', methods=['GET', 'POST'])
def login():
    if request.method == ['POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is None or not user.check_password(request.form.get('password')):
            flash('Either that user does not exist or the pasword is incorrect. Try again.', 'warning')
            return redirect(url_for('login'))
        remember_me = True if request.form.get('checked') is not None else False
        login_user(user, remember=remember_me)
        flash(f'Welcome, {user.first_name} {user.last_name}! You have successfully logged in!', 'sucess')
        return redirect(url_for('home'))
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User()
        u.from_dict(request.form)
        u.save()
        flash('User created successfully', 'info')
        return redirect(url_for('auth.login'))
    return render_template('register.html')
