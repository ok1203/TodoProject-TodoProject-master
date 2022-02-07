from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo-index'),
    path('about/', views.about, name='todo-about')
]

