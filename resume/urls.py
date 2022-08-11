from unicodedata import name
from django.urls import path
from resume.views import *
app_name = 'resume'

urlpatterns = [
    path('', home, name='home'),
    path('resume', pdf_view, name='resume'),
]
