from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main),
    path('posts', views.all_posts),
    path('posts/<name_post>', views.post_details)
]