from . import views
from django.urls import path  ,re_path  
urlpatterns = [
     path("", views.list_docker_images,name="homepage"),
]