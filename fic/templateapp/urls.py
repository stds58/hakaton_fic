
from django.urls import path, include
from .views import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard')
]

