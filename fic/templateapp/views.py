from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import datetime
from .utils import AIRequest
from .task import start_help_filling


class Dashboard(View):
    def get(self, request):
        return render(request,'templateapp/dashboard.html')


class UserRequest(CreateView):
    def get(self, request):
        return render(request,'gigachat.html')
    def post(self, request):
        user_request = request.POST.get('user_query')
        xx = AIRequest(user_request)
        return HttpResponse(xx)


def test_celery(request):
    result = start_help_filling()
    print(result)

    return render(request, 'templateapp/dashboard.html')