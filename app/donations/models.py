from django.db import models

# Create your models here.

class DonationCategory(models.Model):
    name = models.CharField()
    description = models.CharField()

class RequestedDonations(models.Model):
    name = models.CharField()
    amount_needed = models.IntegerField()
    category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE)

class Donor(models.Model):
    address = models.CharField()
    phone_number = models.CharField()
    email_address = models.CharField()
    contact_name = models.CharField()
    organization = models.CharField()
    # key based authfor update?

class DonationOffer(models.Model):
    amount = models.IntegerField()
    donation = models.ForeignKey(RequestedDonation, on_delete=models.CASCADE)

