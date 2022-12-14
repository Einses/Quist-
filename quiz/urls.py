from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('frontend', views.frontend, name='frontend'),
    path('gameloading', views.gameloading, name='gameloading'),
    path('gameend', views.gameend, name='gameend'),
    path('QandA', views.QandA, name='QandA'),
    path('quiz2', views.quiz2, name='quiz2'),
    path('quiz3', views.quiz3, name='quiz3'),
    path('quiz4', views.quiz4, name='quiz4'),
    path('quiz5', views.quiz5, name='quiz5'),

]
