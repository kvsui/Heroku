from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo  

app.config['SECRET_KEY']  = 'KVS'

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
	email= StringField('Email', validatorus=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = Password('Confirm Password', validators = [DataRequired(),EqualTo('password')])
	submit = SubmitField('Signup')



	class LoginForm(FlaskForm):

	email= StringField('Email', validatorus=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login ')