from apps import utils
from django.shortcuts import render, redirect
from apps.models import Submission
from apps.forms import SubmitAppForm
from django.contrib import messages

"""
A user wants to submit an app
"""
def submit_app(request):

	if request.POST:

		app_form = SubmitAppForm(request.POST)

		if app_form.is_valid():

			# Get the email address from teh form
			email_address = app_form.cleaned_data['email_address']

			try:
				submission = Submission.objects.get(email_address=email_address)
				messages.warning(request, "An application has already been submitted for this email address!")
				return redirect('submit-app')
			except:

				instance = app_form.save(commit=False)

				if instance:
					instance.user = request.user
					instance.save()

					messages.success(request, "Thank you for submitting!")
				else:
					messages.warning(request, "Application failed to submit. Make sure the email addresses are valid and you entered the required information.")

			return redirect('submit-app')

	else:
		app_form = SubmitAppForm()

	context = {'form': app_form}
	return render(request, 'app/create.html', context)

def app_details(request, app_id):

	"""
	Get the application for the ID
	"""
	try:
		app = Submission.objects.get(id=app_id)
	except:
		#messages.error(request, 'Could not find app for that ID')
		return redirect('index')


	context = {'app': app}
	return render(request, 'app/app_details.html', context)
	
