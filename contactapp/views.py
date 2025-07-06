from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def contact_view(request):
        if request.method == 'POST':
           name = request.POST.get('name')
           email = request.POST.get('email')
           message = request.POST.get('message')
        
           subject = f'Contact Form Submission from {name}'
           body = f'Email: {email}\n\nMessage:\n{message}'

           send_mail(
               subject,
               body,
               settings.EMAIL_HOST_USER,  
               ['nischal.gautam@aitm.edu.np'],  
               fail_silently=False
            )
        return render(request, 'contact.html')

def index_view(request):
      return render(request,'index.html')

def services_view(request):
      return render(request,'services.html')

def getinvolved_view(request):
      return render(request, 'getinvolved.html')

def event_view(request):
      return render(request,'events.html')

def aboutus_view(request):
      return render(request,'aboutus.html')

