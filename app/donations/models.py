from django.db import models

# Create your models here.

class DonationCategory(models.Model):
    name = models.CharField()
    description = models.CharField()

    def donations(self):
        return RequestedDonation.objects.filter(category=self)

class RequestedDonation(models.Model):
    name = models.CharField()
    amount_needed = models.IntegerField()
    category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE)

    def still_needed(self):
        provided = sum(o.amount
                for o in DonationOffer.objects.filter(donation=self))

        still_needed = self.amount_needed - provided
        if still_needed < 0:
            still_needed = 0
        return still_needed


class Donor(models.Model):
    address = models.CharField()
    phone_number = models.CharField()
    email_address = models.CharField()
    contact_name = models.CharField()
    organization = models.CharField()
    key = models.CharField()

class DonationOffer(models.Model):
    amount = models.IntegerField()
    donation = models.ForeignKey(RequestedDonation, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
