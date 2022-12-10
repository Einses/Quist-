from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('index', views.index, name='index'),
    path('gameloading', views.gameloading, name='gameloading'),
    path('home', views.home, name='home'),
]