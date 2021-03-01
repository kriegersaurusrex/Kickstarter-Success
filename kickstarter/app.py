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
			forms_data=(name,ks_id)
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
