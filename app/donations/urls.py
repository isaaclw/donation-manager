from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.new_contact, name='new_contact'), # new contact
    re_path('contact/(?P<key>[a-zA-Z0-9]{32})/', views.edit_contact, name='edit_contact'),  # update contact
    re_path('donation/(?P<key>[a-z0-9]{32})', views.donation, name='donation'), # submit donation
    ]
