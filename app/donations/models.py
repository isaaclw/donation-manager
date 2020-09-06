from django.db import models

# Create your models here.

class DonationCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    def donations(self):
        return RequestedDonation.objects.filter(category=self)

    def __str__(self):
        return self.name

class RequestedDonation(models.Model):
    name = models.CharField(max_length=30)
    amount_needed = models.IntegerField()
    category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE)

    def still_needed(self):
        provided = sum(o.amount
                for o in DonationOffer.objects.filter(donation=self))

        still_needed = self.amount_needed - provided
        if still_needed < 0:
            still_needed = 0
        return still_needed

    def __str__(self):
        return '%s (%s)' % (self.name, self.amount_needed)


class Donor(models.Model):
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    key = models.CharField(max_length=32)

class DonationOffer(models.Model):
    amount = models.IntegerField()
    donation = models.ForeignKey(RequestedDonation, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
