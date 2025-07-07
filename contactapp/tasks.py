from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_email(subject, body, to_email):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )
