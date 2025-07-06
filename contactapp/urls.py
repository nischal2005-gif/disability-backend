from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', contact_view,name='contact'),
    path('aboutus/', aboutus_view, name='aboutus'),
    path('', index_view, name='home'),
    path('services/', services_view,name='services'),
    path('getinvolved/', getinvolved_view,name='getinvolved'),
    path('events/', event_view,name='events'),

    
    ]