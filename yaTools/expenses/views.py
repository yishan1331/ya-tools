from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .expenses import ExpenseList, ExpenseCategoryList

# Create your views here.


@login_required
def expensesList(request):
    return render(request, 'expenses/list.html')


def classification(request):
    return render(request, 'expenses/classification.html')


def reports(request):
    return render(request, 'expenses/reports.html')
