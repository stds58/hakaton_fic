from django.urls import path, include
from .import views

urlpatterns = [
    path('download_pdf/<int:report_id>', views.generate_pdf_view, name='download_pdf'),
]