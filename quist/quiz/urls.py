from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('frontend', views.frontend, name='frontend'),
    path('gameloading', views.gameloading, name='gameloading'),
    path('gameend', views.gameend, name='gameend'),
]