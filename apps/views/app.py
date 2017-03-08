from apps import utils
from django.shortcuts import render, redirect
from apps.models import Submission
from apps.forms import SubmitAppForm

"""
A user wants to submit an app
"""
def submit_app(request):

	if request.POST:

		app_form = SubmitAppForm(request.POST)

		instance = app_form.save(commit=False)
		instance.user = request.user
		instance.save()

		return redirect('index')

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
	
