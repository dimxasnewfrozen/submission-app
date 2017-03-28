from apps import utils
from django.shortcuts import render, redirect
from apps.models import Submission
from apps.forms import SubmitAppForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import random

order_by = ['name', 'code_url', 'app_url', 'thumbnail_url', 'date_created']

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
			print app_form.errors
	else:
		app_form = SubmitAppForm()

	context = {'form': app_form}
	return render(request, 'app/create.html', context)


def success(request):
	return render(request, 'app/submit_success.html', {})

#@login_required()
def submissions(request):

	request.session.set_expiry(0)

	if 'current_order' in request.session:
		order = request.session['current_order']
	else:
		request.session['current_order'] = random.choice(order_by)
		order = request.session['current_order']

	submissions_list = Submission.objects.all().order_by('name')

	num_of_entries = 5

	paginator = Paginator(submissions_list, num_of_entries)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		submissions = paginator.page(page)
	except(EmptyPage, InvalidPage):
		submissions = paginator.page(paginator.num_pages)

	num_showable_pages = 10
	current_pages_interval = page / num_showable_pages

	if current_pages_interval == 0:
		if submissions.paginator.num_pages < 10:
			page_range = xrange(1, submissions.paginator.num_pages + 1)
		else:
			page_range = xrange(1, 10)
	else:
		if submissions.paginator.num_pages == page:
			page_range = xrange(current_pages_interval * 10, submissions.paginator.num_pages + 1)
		else:
			page_range = xrange(current_pages_interval * 10, (current_pages_interval + 1) * 10)

	context = {'submissions': submissions, 'page_range': page_range}
	return render(request, 'app/submissions.html', context)

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
	
