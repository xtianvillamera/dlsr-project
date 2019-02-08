from django.urls import path
from .views import StudentListView, StudentDetailView
from . import views

urlpatterns = [
    path('', StudentListView.as_view(), name="Students-StudentsList"),
    path('s/<int:pk>/', StudentDetailView.as_view(),name='s-detail'),
]