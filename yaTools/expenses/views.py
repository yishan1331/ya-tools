from django.shortcuts import render
from django.http import HttpResponse
from .expenses import ExpenseCreate, ExpenseCategoryList

# Create your views here.


def keeping(request):
    return render(request, 'expenses/keeping.html')


def classification(request):
    return render(request, 'expenses/classification.html')


def reports(request):
    return render(request, 'expenses/reports.html')
