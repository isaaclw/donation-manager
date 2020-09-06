from django.shortcuts import render

from .models import DonationCategory

# Create your views here.
def home(request):
    categories = DonationCategory.objects.all()

    return render(request, 'donations/home.html', {
            'categories': categories,
        })
