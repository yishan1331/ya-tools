from django.conf.urls import url
from django.urls import path
from expenses import views

urlpatterns = [
    path('', views.ExpenseList.as_view(),
         name='expenses_list'),
    path('classification/', views.classification,
         name='expenses_classification'),
    path('reports/', views.reports, name='expenses_reports'),
]
