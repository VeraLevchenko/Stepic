from django.urls import path
from . import views

urlpatterns = [
	path('rectangle/<int:w>/<int:h>', views.get_rectangle_area),
	path('square/<int:h>', views.get_square_area),
	path('circle/<int:r>', views.get_circle_area),
]