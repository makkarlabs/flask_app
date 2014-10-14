from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SelectField, DecimalField, IntegerField, DateField, BooleanField, TextAreaField, HiddenField
from flask_security.forms import RegisterForm, LoginForm
from wtforms.validators import Required, Regexp, Length, Email, URL, EqualTo, NumberRange
from flask_wtf import RecaptchaField
from {% flask_app.name %} import config

class ExtendedRegisterForm(RegisterForm):
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])
    organization = TextField('Organisation', [Required()])
    recaptcha = RecaptchaField()


