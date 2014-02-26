from django.contrib import admin
from rct.models import CustomUserManager, CustomUser


admin.site.register(CustomUser)
