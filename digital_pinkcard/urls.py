from django.urls import path
from .views import *
from . import views

urlpatterns = [
	path('', views.testing),
	path('login/', views.login),
]