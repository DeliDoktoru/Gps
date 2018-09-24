from django.contrib import admin

from .models import Employer,Employee

admin.site.register([Employer,Employee])
