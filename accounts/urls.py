from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('treasure/', views.treasure, name='treasure'),
    path('register/', views.register, name='register'),
]
