from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from django.contrib.auth.models import User

"""
The auth
"""
def auth(request):

	if request.POST:

		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = authenticate(username=username, password=password)
		if user is not None:
		    # A backend authenticated the credentials
			return redirect('submissions')
		else:
			messages.error(request, 'Could not find an account with this info.')
			return redirect('login')

	else:
		form = AuthenticationForm()

	context = {'form': form}
	return render(request, 'signin.html', context)
