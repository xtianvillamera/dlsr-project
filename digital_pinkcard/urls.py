from django.urls import path
from .views import *
from . import views

urlpatterns = [
	path('', views.testing),
	path('login/', LogIn.as_view(), name='LogIn'),
	path('user/<int:pk>/', UserDetailView.as_view(), name='pinkcard-UserDetailView'),
]