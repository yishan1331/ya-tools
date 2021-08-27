from django.shortcuts import render
from django.contrib import auth

# Create your views here.

# 首頁


def index(request):
    return render(request, 'index.html')

# 登出


def log_out(request):
    logout(request)
    return redirect('/login')
