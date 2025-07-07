from .models import Event
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        secret_key = '6LfIjXorAAAAAMGK5XwY3wAOwbD89BVvn5UgyyEm'

        # Verify reCAPTCHA
        data = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result.get('success'):
            # If verified, process the form
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            subject = f'Contact Form Submission from {name}'
            body = f'Email: {email}\n\nMessage:\n{message}'

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,  
                ['nischalgautam9866@gmail.com'],  
                fail_silently=False
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Adjust the redirect as needed
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('contact')

    return render(request, 'contact.html')


def index_view(request):
      return render(request,'index.html')

def services_view(request):
      return render(request,'services.html')

def getinvolved_view(request):
      return render(request, 'getinvolved.html')

def event_view(request):
    # Past events = is_upcoming = False
    past_events = Event.objects.filter(is_upcoming=False).order_by('-date')

    # Upcoming events = is_upcoming = True
    upcoming_events = Event.objects.filter(is_upcoming=True).order_by('date')

    context = {
        'past_events': past_events,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'events.html', context)

def aboutus_view(request):
      return render(request,'aboutus.html')

