import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired, Regexp, ValidationError, Email, Length, EqualTo, Optional, DataRequired

from models import User


WSCENTERS = [
    ("Ohio-Kentucky-Indiana", "Ohio-Kentucky-Indiana Water Science Center"),
    ("Illinois", "Illinois Water Science Center"),
    ("California", "California Water Science Center"),
]


def email_exists(form, field):
    if User.query.filter_by(User.email == field.email.data).first():
        raise ValidationError("User with that email already exists.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class RegisterForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message=("Please enter a valid email address.")),
        ])

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message=("Passwords must have a minimum of 8 characters."))
        ])

    # wsc = SelectField(
    #     "Water Science Center",
    #     choices=WSCENTERS,
    #     validators=[
    #         DataRequired()
    #     ])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')

    def validate(self):
        if not super().validate():
            return False
        return True



