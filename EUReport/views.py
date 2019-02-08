from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Semester, DeptInst

# Create your views here.
def EURHome(request):
	context = {
		'deptsinsts': DeptInst.objects.all(),
		'sems': Semester.objects.all()
	}
	return render(request,'EUReport/EURPage.html')

class ReportListView(ListView):
	model = DeptInst
	template_name = 'EUReport/EURPage.html'
	context_object_name = 'deptsinsts'