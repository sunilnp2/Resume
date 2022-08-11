from django.shortcuts import render, redirect
from resume.models import Contact
from django.contrib import messages
from django.http import FileResponse
import os

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        em = request.POST['myemail']
        message = request.POST['message']
        
        if not name:
            messages.error(request, 'Name field is required')
            return redirect('/')

        elif not em:
            messages.error(request, 'email field is required')
            return redirect('/')
            
        elif not message:
            messages.error(request, 'message field is required')
            return redirect('/')
        else:
            con = Contact.objects.create(name = name,email = em, message = message)
            con.save()
            messages.success(request, "Message Sent Successfully!")
            return redirect('resume:home')
    return render(request, 'index.html')




# def viewpdf(request):
#     # pdf = render_t
#     return HttpResponse('resume.pdf', content_type = 'application/pdf')


 
# def showpdf(request):
#     filepath = os.path.join('static', 'resume.pdf')
#     return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

from django.http import  HttpResponse
def pdf_view(request):
    with open('resume.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response