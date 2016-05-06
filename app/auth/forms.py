from flask.ext.wtf import Form
from wtforms import StringFiled, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email

class LoginForm(Form):
    email = StringFiled('Email', validators = [Required(), Length(1, 64), Email()])