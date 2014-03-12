from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rct.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login(request):
	context = RequestContext(request)
	return render_to_response('rct/login.html',context)

def index(request):
	context = RequestContext(request)
	return render_to_response('rct/index.html',context)

def projectBoard(request):
	context = RequestContext(request)
	return render_to_response('rct/projectBoard.html',context)
	
def signup(request):
	context = RequestContext(request)

	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			registered = True
			return HttpResponseRedirect('/rct/login')
		else:
			print user_form.errors
	else:
		user_form = UserForm()

	return render_to_response('rct/signup.html',{'user_form': user_form , 'registered':registered},context)


def loginManual(request):

	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				loginManual(request,user)
				return HttpResponseRedirect('/rct/')
			else:
				return HttpResponse("Inactive account used!")
		else:
			return HttpResponse("Invalid login details")
	else:
		return render_to_response('rct/loginManual.html',context)

