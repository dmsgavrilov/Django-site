from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('add-task', views.add_task, name="add-task"),
    path('upload-file', views.upload_file, name="upload-file"),
    path('find-file', views.find_file, name="find-file"),
    path('find-file/<str:path>', views.download, name="download"),
]