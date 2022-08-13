from django.conf.urls import url
from django.urls import path
from expenses import views

urlpatterns = [
    path('', views.ExpenseCategoryList.as_view(),
         name='expenses_keeping'),
    path('classification/', views.classification,
         name='expenses_classification'),
    path('reports/', views.reports, name='expenses_reports'),
]
