from django.shortcuts import render
from portfolio.models import Portfolio
from services.models import Services
from review.models import Review

# Create your views here.
def index(request):
    portfolio = Portfolio.objects.order_by('-id')[:3]
    services = Services.objects.order_by('-id')[:3]
    review = Review.objects.order_by('-id')[:3]
    data = {
        'portfolio': portfolio,
        'services': services,
        'review': review,
    }
    return render(request, 'index.html', context=data)