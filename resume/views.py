from django.shortcuts import render, redirect
from resume.models import Contact
from django.contrib import messages

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