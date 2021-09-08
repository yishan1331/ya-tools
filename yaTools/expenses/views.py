from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def keeping(request):
    return render(request, 'expenses/keeping.html')


def settings(request):
    return render(request, 'expenses/settings.html')


def reports(request):
    return render(request, 'expenses/reports.html')
