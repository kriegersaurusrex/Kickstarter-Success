import pandas as pd
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField



# KickStarter info form class definition
class KickStarterForm(FlaskForm):
	kickstarter_name = StringField(label='Name of Kickstarter Campaign')
	kickstarter_id = StringField(label='Campaign ID')
	submit = SubmitField('SUBMIT')



   