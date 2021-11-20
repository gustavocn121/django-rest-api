

from django.urls.conf import path
from django.urls import path
from seazone_api import views

urlpatterns = [
    path('', views.CalendarApi.as_view(), name='index'),
    
]