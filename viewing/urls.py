from django.urls import path
from .views import *
from . import views

urlpatterns = [
	path('', views.Home, name="viewing-Home"),
	path('deg_prog/', DegProgListView.as_view(), name="viewing-ViewingDegProgList"),
	#path('deg_prog/<int:pk>/', DegProgDetailView.as_view(), name="viewing-DegProgDetailView"),
	path('deg_prog/<int:pk>/', DegProgStudentList.as_view(), name="viewing-DegProgStudentList"),
	path('elec_usage/', ElecUsageListView.as_view(), name="viewing-ElecUsageListView"),
	path('student/<int:pk>/', StudentDetailView.as_view(), name='viewing-StudentDetailView'),
	path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='viewing-StudentUpdateView'),
	path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='viewing-StudentDeleteView'),
	path('student/new/',StudentCreateView.as_view(), name='viewing-StudentCreate')
]