from django.contrib import admin
from .models import Module

admin.site.site_header = 'Biomed Admin Panel'
admin.site.site_title = 'Biomed'

# Register your models here.
admin.site.register(Module)
