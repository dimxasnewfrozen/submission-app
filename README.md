# MadGlory Hackathon Submissions App
	This app will allow participants of MadGlory hosted hackathons to submit their applications

### Prerequisites
	Install Python 2.7
	Install MySQL

### Setup

	# Create virtual environment to keep track of dependencies
	virtualenv --no-site-packages ve_submission_app

	# Activate the virtual environment
	source ve_submission_app/bin/activate

	# Install dependencies
	pip install -r requirements.txt

	# Build database by running migrations
	# Not necessary if you already have your database built
	python manage.py migrate

	# Install fixture data
	# This is sample data that defines some of the structures
	python manage.py loaddata app_type
	python manage.py loaddata game

### Start test app server
	python manage.py runserver
