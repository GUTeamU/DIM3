from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rct.forms import UserForm, ProjectForm, TaskForm, EditProjectForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from rct.models import Project, Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def is_member(project, user_id):
    for m in project.members.all():
        if m.id == user_id:
            return True

    return False


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

@login_required
def index(request):
    context = RequestContext(request)

    projects = []
    for p in Project.objects.all():
        if is_member(p, request.user.id):
            projects.append(p)

    for p in projects:
        p.url = p.name.replace(' ', '_').lower()

    context_dict = {'projects' : projects}
    return render_to_response('rct/index.html', context_dict, context)

def edit_project(request, url):
    context = RequestContext(request)

    project = Project.objects.get(url=url)
    if not is_member(project, request.user.id):
        HttpResponse("Access denied")

    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid():
                project = form.save()

    return HttpResponseRedirect(reverse('rct.views.view_project', args=(url,)))

@login_required
def create_project(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=True)
            project.url = project.name.replace(' ', '_').lower()
            user = User.objects.get(pk=request.user.id)
            project.members.add(user)
            project.save()

            return HttpResponseRedirect(reverse('rct.views.projectBoard'))

    else:
        form = ProjectForm()

    return render_to_response('rct/projects/create.html', {'form':form}, context)

@login_required
def view_project(request, url):
    context = RequestContext(request)
    context_dict = {}

    try:
        project = Project.objects.get(url=url)
        if not is_member(project, request.user.id):
            return HttpResponse("Access denied")

        context_dict['project'] = project
        context_dict['form']  = EditProjectForm(instance=project)
    except Project.DoesNotExist:
        return HttpResponseNotFound('<h1>Project not found</h1>')

    try:
        for key in ('must', 'should', 'could', 'would'):
            context_dict[key] = context_dict['project'].task_set.filter(category=key[0].upper()).all()
    except Exception:
        # guess there are no tasks
        pass    

    return render_to_response('rct/projects/view.html', context_dict, context)

@login_required
def add_task(request, url):

    context = RequestContext(request)
    context_dict = {}
    try:
        project = Project.objects.get(url=url)
        if not is_member(project, request.user.id):
            return HttpResponse("Access denied")

        context_dict['project'] = project
    except Project.DoesNotExist:
        pass

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = context_dict['project']
            task.save()

            return HttpResponseRedirect(reverse('rct.views.index') + "project/" + url)
    else:
        form = TaskForm()
    context_dict['form'] = form
    return render_to_response('rct/tasks/create.html', context_dict, context)

@login_required
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

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rct/login')

@login_required
def delete_task(id):
    toDelete = Task.objects.filter(id=id)
    toDelete.delete()

@login_required
def delete_project(request,url):

    project = Project.objects.get(url=url)
    if not is_member(project, request.user.id):
        return HttpResponse("Access denied")

    Project.objects.filter(url=url).delete()
    return HttpResponseRedirect('/rct/')
