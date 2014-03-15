from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rct.forms import UserForm, ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from rct.models import Project
from django.contrib.auth.models import User

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		
		user = User.objects.get(email=email)
		if(user.password=="!"):
			print "Social Auth"
		
		auth = authenticate(username=user, password=password)

		if auth is not None:
			if auth.is_active:
				login(request, auth)
				return HttpResponseRedirect('/rct/')
			else:
				return HttpResponse("Inactive account used!")
		else:
			return HttpResponse("Invalid login details")	
	return render_to_response('rct/login.html',context)

def index(request):
	context = RequestContext(request)

        projects = Project.objects.all()
        context_dict = {'projects' : projects}
        
        for p in projects:
            p.url = p.name.replace(' ', '_').lower()

	return render_to_response('rct/index.html', context_dict, context)

def create_project(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse('rct.views.index'))

    else:
        form = ProjectForm()

    return render_to_response('rct/projects/create.html', {'form':form}, context)

def view_project(request, url):
    context = RequestContext(request)
    context_dict = {}

    try:
        context_dict['project'] = Project.objects.get(name__iexact=url.replace('_', ' '))
    except Project.DoesNotExist:
        # TODO redirect to 404
        pass

    return render_to_response('rct/projects/view.html', context_dict, context)

## Broken function
def add_task(request,url):

	context = RequestContext(request)
	context_dict = {}
	try:
		context_dict['project'] = Project.objects.get(name__iexact=url.replace('_',' '))
	except Project.DoesNotExist:
		pass
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect(reverse('rct.views.index'))
	else:
		form = TaskForm()
	return render_to_response('rct/tasks/create.html', {'form':form}, context)


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

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rct/login')