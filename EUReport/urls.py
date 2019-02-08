from django.urls import path
from .views import ReportListView
from . import views

urlpatterns = [
    path('', ReportListView.as_view(), name="EUReport-EURPage"),
]