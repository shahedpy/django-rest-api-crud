from django.contrib import admin
from .models import Students, Departments, Sessions

# Register your models here.
admin.site.register(Students)
admin.site.register(Departments)
admin.site.register(Sessions)
