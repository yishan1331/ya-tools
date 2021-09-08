from django.conf.urls import url
from django.urls import path
from expenses import views

urlpatterns = [
    path('', views.keeping, name='expenses_keeping'),
    path('settings/', views.settings, name='expenses_settings'),
    path('reports/', views.reports, name='expenses_reports'),
]
