from django.contrib import admin
from .models import DonationCategory
from .models import RequestedDonation

# Register your models here.
admin.site.register(DonationCategory)
admin.site.register(RequestedDonation)
