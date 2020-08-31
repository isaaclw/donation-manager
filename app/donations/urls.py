from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'), # new contact
    path('contact/(?P<key>)', views.contact, name='contact'),  # update contact
    path('donation/(?P<key)', views.donation, name='donation'), # submit donation
    ]
