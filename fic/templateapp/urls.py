
from django.urls import path, include
from .views import Dashboard, UserRequest

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('gigachat/', UserRequest.as_view(), name='gigachat')
]

