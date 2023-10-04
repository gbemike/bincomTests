from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path("edit-task/<str:pk>/", views.editTask, name="edit-task"),
    path("delete-task/<str:pk>/", views.deleteTask, name="delete-task"),
]
