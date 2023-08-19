from django.urls import path
from . import views

urlpatterns = [
	path('<int:day>/', views.day_info_by_number),
	path('<day>/', views.day_info),
]
