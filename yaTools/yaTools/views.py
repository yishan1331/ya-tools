from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# 首頁


@login_required
def index(request):
    return render(request, 'index.html')


# 登出


def log_out(request):
    logout(request)
    return redirect('/login')
