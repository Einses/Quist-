from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('index', views.index, name='index'),

]