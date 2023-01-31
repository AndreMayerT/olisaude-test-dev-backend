from django.contrib import admin

from .models import Client, HealthProblem

# Register your models here.

admin.site.register(Client)
admin.site.register(HealthProblem)