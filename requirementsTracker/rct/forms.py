from rct.models import UserProfile, Project, Task
from django.contrib.auth.models import User
from django import forms
from datetimewidget.widgets import DateTimeWidget


CATEGORIES=[('M', 'Must Have'),('S', 'Should Have'),('C', 'Could Have'),('W', 'Would Like')]

dateTimeOptions = {
'format': 'dd/mm/yyyy',
'minView': '2',
'todayHighlight': 'true'
}

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
	title = forms.CharField(max_length=256,help_text= "Enter a title")
	deadline = forms.DateTimeField(widget=DateTimeWidget(usel10n = True, options=dateTimeOptions), help_text="Deadline, click to open widget")
	category = forms.ChoiceField(choices = CATEGORIES, widget=forms.Select())

	class Meta:
		model = Task
		fields = ('title', 'deadline', 'description', 'category')

class EditTaskForm(TaskForm):
    deadline = forms.CharField()

    class Meta:
        model = Task
        fields = ('title', 'deadline', 'category', 'description', 'completed')
