from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SignupForm(FlaskForm):
    """User signup form."""

    name = StringField("Name", validators=[DataRequired()])

    email = StringField("Email", validators=[Email("Enter a valid email"),
                                             DataRequired()])

    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, message="Password is not strong enough")])

    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])

    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    """Login form"""
    email = StringField("Email", validators=[Email("Enter a valid email"),
                                             DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField("Sign up")
