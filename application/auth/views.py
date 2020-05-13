from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import UserMixin, login_user, current_user, logout_user
from flask import Blueprint

from application import db, login_manager
from .forms import SignupForm, LoginForm
from .models import User

auth_bp = Blueprint('auth_bp',
                    __name__,
                    template_folder="templates",
                    static_folder="static",
                    url_prefix="/auth")


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET: Serve sign-up page.
    POST: If submitted credentials are valid, redirect user to the logged-in homepage.
    """
    # signup_form = SignupForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()  # Check if user exists
        if existing_user is None:
            user = User()
            user.name = name
            user.email = email
            user.set_password(password)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('dashboard_bp.home'))
        flash('A user already exists with that email address.')
        return redirect(url_for('auth_bp.signup'))

    return render_template('auth_signup.html',
                           title='Create an Account.',
                           form=SignupForm(),
                           template='signup-page',
                           body="Sign up for a user account.")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login page.

    GET: Serve Log-in page.
    POST: If form is valid and new user creation succeeds, redirect user to the logged-in homepage.
    """
    if current_user.is_authenticated:
        return redirect(url_for('resource_bp.index'))  # Bypass if user is logged in

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()  # Validate Login Attempt
        if user and user.check_password(password=password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard_bp.home'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login'))

    return render_template('auth_login.html',
                           form=LoginForm(),
                           title='Log in.',
                           template='login-page',
                           body="Log in with your User account.")


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
