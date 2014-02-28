from django.contrib import admin
from rct.models import CustomUserManager, CustomUser, Project, Task

admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Task)
