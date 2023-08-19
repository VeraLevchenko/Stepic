from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('leo/', views.leo),
    path('aries/', views.aries),
    path('taurus/', views.taurus),
	]
