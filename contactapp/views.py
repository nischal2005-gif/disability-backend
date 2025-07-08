from .models import *
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import cache_page
from contactapp.tasks import send_contact_email
from celery import shared_task

def contact_view(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        secret_key = '6LfIjXorAAAAAMGK5XwY3wAOwbD89BVvn5UgyyEm'

        data = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result.get('success'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            subject = f'Contact Form Submission from {name}'
            body = f'Email: {email}\n\nMessage:\n{message}'

            send_contact_email.delay(subject,body,'nischalgautam9866@gmail.com')
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact') 
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('contact')

    return render(request, 'contact.html')


def index_view(request):
      return render(request,'index.html')
@cache_page(60*3)
def services_view(request):
      services=Service.objects.all()
      return render(request,'services.html',{'services':services})

def getinvolved_view(request):
      return render(request, 'getinvolved.html')

@cache_page(60*5)
def event_view(request):
    past_events = Event.objects.filter(is_upcoming=False).order_by('-date')
    upcoming_events = Event.objects.filter(is_upcoming=True).order_by('date')

    context = {
        'past_events': past_events,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'events.html', context)

def aboutus_view(request):
      return render(request,'aboutus.html')

def contribute_view(request):
     return render(request,'contribute.html')

