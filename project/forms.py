from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DaraRequired, Length

var regex = '/^\d+(?:\.\d{0,2})$/'

class RegistrationForm(FlaskForm):
	gallons = Regexp(regex
	name 	= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email 	= StringField('Email', validators=[DataRequired(0, Email())])