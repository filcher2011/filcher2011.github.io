from django.contrib import admin
from portfolio.models import Portfolio
from services.models import Services
from review.models import Review

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Services)
admin.site.register(Review)