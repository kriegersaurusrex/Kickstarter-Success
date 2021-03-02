import pandas as pd
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField,\
				StringField, SelectField, DecimalField,\
				DateTimeField
from wtforms.validators import DataRequired, ValidationError



BOOLEAN = ['YES','NO']
LOCATION_TYPE = ['Town', 'Zip', 'County', 'Suburb', 'LocalAdmin', 'Island']
LOCATION_COUNTRY = ['United States', 'United Kingdom', 'Canada', 'New Zealand',
       'Sweden', 'Germany', 'Taiwan', 'Greece', 'Netherlands',
       'Australia', 'Japan', 'Thailand', 'Switzerland', 'Mexico', 'Kenya',
       'Italy', 'Denmark', 'China', 'Singapore', 'Hong Kong', 'France',
       'Argentina', 'Norway', "Cote d'Ivoire", 'Ireland', 'Spain',
       'Ecuador', 'Russia', 'Belgium', 'Nigeria', 'Haiti', 'South Korea',
       'Hungary', 'Guatemala', 'Egypt', 'Jamaica', 'Nicaragua', 'Peru',
       'Viet Nam', 'Dominican Republic', 'Myanmar', 'Austria', 'Lebanon',
       'India', 'Puerto Rico', 'Iceland', 'Czech Republic', 'Nepal',
       'Svalbard and Jan Mayen', 'Bulgaria', 'Poland', 'Romania',
       'Malaysia', 'Lithuania', 'Belize', 'Belarus', 'Ukraine',
       'Portugal', 'Chile', 'Philippines', 'South Africa', 'Serbia',
       'Estonia', 'Costa Rica']
CURRENCY = ['USD', 'GBP', 'CAD', 'NZD', 'EUR', 'AUD', 'CHF', 'MXN', 'DKK',
       'SGD', 'HKD', 'NOK', 'JPY', 'SEK']

def validate_currency(form, field):
	if field.data < 10.2:
		print('Validation Error encountered')
		raise ValidationError('You need to enter currency data only')

# KickStarter info form class definition
class KickStarterForm(FlaskForm):
	kickstarter_name = StringField(
		label='Name of Kickstarter Campaign', 
		validators=[DataRequired()])
	kickstarter_id = StringField(label='Campaign ID', validators=[DataRequired()])
	kickstarter_staffpick = SelectField(label='Staff Pick', choices=BOOLEAN)
	kickstarter_spotlight = SelectField(label='Spot Light', choices=BOOLEAN)
	kickstarter_locationtype= SelectField(label='Location Type', choices=LOCATION_TYPE)
	kickstarter_country= SelectField(label='Country', choices=LOCATION_COUNTRY)
	kickstarter_currency= SelectField(label='Currency', choices=CURRENCY)
	kickstarter_usdgoal = DecimalField(
		label='USD Goal  ', 
		validators=[DataRequired(), validate_currency], render_kw={"placeholder": "$00.00"})
	kickstarter_usdpledge = DecimalField(
		label='USD Pledge  ', 
		validators=[DataRequired(), validate_currency], render_kw={"placeholder": "$00.00"})
	kickstarter_creatorid = StringField(label='Creator ID')
	kickstarter_creatorname = StringField(label='Creator name')
	kickstarter_locationid = StringField(label='Creator name')
	
	submit = SubmitField('SUBMIT')



   