from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django import forms

from .models import DonationCategory
from .models import Donor

# Create your views here.
def home(request):
    categories = DonationCategory.objects.all()

    return render(request, 'donations/home.html', {
            'categories': categories,
        })

class ContactForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['contact_name', 'organization', 'address', 'phone_number',
                'email_address']


def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            d = form.save()
            return redirect(
                    reverse('edit_contact', kwargs={'key': d.key}))
    else:
        form = ContactForm()

    return render(request, 'donations/contact.html', {
        'form': form,
        'key': None,
        })

def edit_contact(request, key=None):
    donor = Donor.objects.get(key=key)

    if request.method == 'POST':
        form = ContactForm(instance=donor, data=request.POST)
        if form.is_valid():
            d = form.save()
    else:
        form = ContactForm(instance=donor)

    return render(request, 'donations/contact.html', {
        'form': form,
        'key': donor.key,
        })
