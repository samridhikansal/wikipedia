from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("home", views.pages , name= "homepage"),
    path("topic/<int:id>", views.topic, name= "topic"),
    path("topic/like/<int:id>", views.like, name= "like"),
    path("topic/dislike/<int:id>", views.topic, name= "dislike"),
    path("search", views.search, name = "search"),
    path("random", views.random_topic, name = "random"),
    path("add", views.add, name = "add"),
    path("edit/<int:id>", views.edit , name = "edit"),
    path("delete/<int:id>", views.delete, name = "delete"),
  
]