
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')#/polls/views.index
]