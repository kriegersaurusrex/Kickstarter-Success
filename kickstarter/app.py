import pandas as pd 
import numpy as np 
import pickle
from flask import Flask, redirect, url_for, render_template
import os
from .forms import KickStarterForm
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.ensemble import RandomForestRegressor
from dotenv import load_dotenv


load_dotenv()


def create_app():
	app = Flask(__name__)
	# Set secret key in your environment variables #
	app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

	@app.route('/')
	def index():
		return redirect(url_for('home'))

	@app.route('/home')
	def home():
		return render_template('home.html')


	@app.route('/run_model', methods=['GET','POST'])
	def run_model():
		form = KickStarterForm()
		if form.validate_on_submit():
			print('Validating form data')
			name = form.kickstarter_name.data
			ks_id = form.kickstarter_id.data
			ks_blurb = form.kickstarter_blurb.data
			ks_created = form.kickstarter_created.data
			ks_lunched = form.kickstarter_launched.data
			ks_deadline = form.kickstarter_deadline.data
			ks_staffpick = form.kickstarter_staffpick.data
			ks_locationtype = form.kickstarter_locationtype.data
			ks_locationstate = form.kickstarter_locationstate.data
			ks_country = form.kickstarter_country.data
			ks_currency = form.kickstarter_currency.data
			ks_creatorid = form.kickstarter_creatorid.data
			ks_usdgoal = form.kickstarter_usdgoal.data
			ks_usdpledge = form.kickstarter_usdpledge.data
			ks_creatorid = form.kickstarter_creatorid.data
			ks_creatorname = form.kickstarter_creatorname.data
			ks_locationid = form.kickstarter_locationid.data
			ks_spotlight = form.kickstarter_spotlight.data
			ks_categoryname = form.kickstarter_categoryname.data
			ks_categoryslug = form.kickstarter_categoryslug.data
			ks_categoryparentid = form.kickstarter_categoryparentid.data
			ks_categoryposition = form.kickstarter_categoryposition.data

			# This is where you enter all of this data into your model    #
			# Note, still testing entry data to see what output types are #
			return redirect(url_for('display_results'))

		return render_template('run_model.html', form=form)



	@app.route('/display_results')
	def display_results():
		return render_template('home.html')


	@app.route('/about')
	def about_page():
		return render_template('about.html')


	return app

if __name__ == "__main__":
	create_app()

