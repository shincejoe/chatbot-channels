from django.contrib import admin

# Register your models here.
from .models import Users, Clicks

admin.site.register(Users)
admin.site.register(Clicks)