from flask.ext.wtf import Form
from wtforms import StringFiled, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length(), Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(Form):
    email = StringFiled('Email', validators = [Required(), Length(1, 64), Email()])
    username = StringFiled('Username', validators = [
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, '
            'numbers, dots or underscores')])
    password = PasswordField('Password', validators = [Required(), EqualTo('password2', message = 'password must match')])
    password2 = PasswordField('Confirm password', validators = [Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registerd.')

    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already in use.')

            
class LoginForm(Form):
    email = StringFiled('Email', validators = [Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators = [Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')