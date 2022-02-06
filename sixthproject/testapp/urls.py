from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.show_view1),
    path('second/', views.show_view2),
    path('third/', views.show_view3),
]
