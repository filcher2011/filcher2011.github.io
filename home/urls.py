from home.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    #path('admin/', admin.site.urls),
]