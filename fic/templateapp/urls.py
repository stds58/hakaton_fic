
from django.urls import path, include
from .views import Dashboard, UserRequest, test_celery

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('gigachat/', UserRequest.as_view(), name='gigachat'),
    path('api_test/', test_celery, name="start_filling")
]

