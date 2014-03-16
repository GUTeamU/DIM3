from rct.models import UserProfile, Project, Task
from django.contrib.auth.models import User
from django import forms
from datetimewidget.widgets import DateTimeWidget

PRIORITIES=[('M', 'Must Have'),('S', 'Should Have'),('C', 'Could Have'),('W', 'Would Like')]

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ('username', 'password', 'first_name','last_name','email')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description')

class TaskForm(forms.ModelForm):

	title = forms.CharField(max_length=32,help_text= "Enter a title")
	deadline = forms.DateTimeField(widget=DateTimeWidget(usel10n = True), help_text="Deadline")
	description = forms.CharField(max_length=256,help_text= "Enter a description")
	priority = forms.ChoiceField(choices = PRIORITIES, widget=forms.RadioSelect())
	category = forms.CharField(max_length=32, help_text= "Enter the type of task")
	class Meta:
		model = Task
