from django.urls import path
from . import views

urlpatterns = [
    path('noticias/', views.noticias, name='noticias'),
]