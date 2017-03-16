from apps import utils
from django.shortcuts import render, redirect
from apps.models import Submission
from apps.forms import SubmitAppForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

"""
Display a list of apps that have been submitted
TODO: Remove @login_required() decorator when submissions are live
"""
@login_required()
def apps(request):
	# Get all of the submissions:
	submissions = Submission.objects.all()

	context = {'apps': submissions}
	return render(request, 'app/apps.html', context)

"""
App details page, showing additional content about the app
TODO: Remove @login_required() decorator when submissions are live
"""
@login_required()
def app_details(request, app_id):

	"""
	Get the application for the ID
	"""
	try:
		app = Submission.objects.get(id=app_id)
	except:
		return redirect('index')

	context = {'app': app}
	return render(request, 'app/app_details.html', context)
	
"""
A user wants to submit an app
"""
def submit_app(request):

	if request.POST:

		app_form = SubmitAppForm(request.POST)

		if app_form.is_valid():

			instance = app_form.save(commit=False)

			if instance:
				instance.user = request.user
				instance.save()
				return redirect('success')
			else:
				messages.warning(request, "Application failed to submit. Make sure the email addresses are valid and you entered the required information.")

			return redirect('submit-app')

	else:
		app_form = SubmitAppForm()

	context = {'form': app_form}
	return render(request, 'app/create.html', context)

"""
A success page when the user has created their app
"""
def success(request):
	return render(request, 'app/submit_success.html', {})