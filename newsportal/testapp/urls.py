from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movies/', views.show_movie),
    path('sports/', views.show_sports),
    path('politics/', views.show_politics),
]
