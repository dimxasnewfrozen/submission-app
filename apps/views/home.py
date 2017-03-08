from django.shortcuts import render
from apps.models import Submission

"""
The home page
"""
def index(request):

	# Get all of the submissions:
	submissions = Submission.objects.all()

	context = {'apps': submissions}
	return render(request, 'index.html', context)
