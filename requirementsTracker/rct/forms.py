from rct.models import UserProfile, Project, Task
from django.contrib.auth.models import User
from django import forms
from datetimewidget.widgets import DateTimeWidget


CATEGORIES=[('M', 'Must Have'),('S', 'Should Have'),('C', 'Could Have'),('W', 'Would Like')]


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ('username', 'password', 'first_name','last_name','email')


class ProjectForm(forms.ModelForm):
	name = forms.CharField(max_length=32,help_text= "Enter a name for your project")
	description = forms.CharField(max_length=256,help_text= "Enter a description")

	class Meta:
		model = Project
		fields = ('name', 'description')

class EditProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('description', 'members')


class TaskForm(forms.ModelForm):
	title = forms.CharField(max_length=32,help_text= "Enter a title")
	completed = forms.BooleanField(initial=False, required=False, help_text="Tick to indicate if task is completed")
	deadline = forms.DateTimeField(widget=DateTimeWidget(usel10n = True), help_text="Deadline, click to open widget")
	description = forms.CharField(max_length=256,help_text= "Enter a description")
	priority = forms.IntegerField(min_value=1, max_value=5, help_text= "Enter the priority of the task (1 highest priority, 5 lowest priority")
	category = forms.ChoiceField(choices = CATEGORIES, widget=forms.RadioSelect())

	class Meta:
		model = Task
		fields = ('title', 'completed', 'deadline', 'description', 'priority', 'category')
