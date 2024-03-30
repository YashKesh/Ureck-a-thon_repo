from . import views
from django.urls import path  ,re_path  
urlpatterns = [
    path("", views.list_docker_images,name="homepage"),
    path('pull-image/', views.pull_image, name='pull_image'),
    path('containers/<str:repository>/', views.container_list, name='container_list'),
    path('create-container/',views.create_container,name = 'create_container'),
    re_path(r'^container-list/(?P<repository>.+)/$', views.container_list, name='container_list'), 
    path('start-container/<str:container_id>/', views.start_container, name='start_container'),
    path('stop-container/<str:container_id>/', views.stop_container, name='stop_container'),  

     
]