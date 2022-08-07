from django.contrib import admin
from resume.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_display_links = ['name', 'email', 'message']
    
admin.site.register(Contact, ContactAdmin)