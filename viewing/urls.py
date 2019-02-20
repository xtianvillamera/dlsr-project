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

]