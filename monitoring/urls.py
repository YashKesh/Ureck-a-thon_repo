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
    path('delete-container/<str:container_id>/', views.delete_container, name='delete_container'),  
     path('delete-image/', views.delete_image, name='delete_image'),
     path('all-containers/', views.all_containers, name='all_containers'),
     path('analysis_board/', views.analysis_board, name='analysis_board'),
     path('analysis_update/',views.analysis_update,name='analysis_update'),
     path('container/<str:container_id>/', views.container_analysis, name='container_analysis'),
     path('container_update/<str:container_id>/', views.container_update, name='container_update'),
     
]