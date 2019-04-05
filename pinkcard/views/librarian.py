from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.views.generic import (ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import *
from ..forms import *

class LibrarianSignUpView(CreateView):
    model = User
    form_class = LibrarianSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'librarian'
        return super().get_context_data(**kwargs)

def Home(request):
	return render(request, 'pinkcard/home.html')

@login_required
def ViewingDegProg(request):
	context = {
		'deg_prog': DegreeProg.objects.all(),
		'students': Student.objects.all()
	}

class DegProgListView(ListView):
	model = DegreeProg
	template_name = 'pinkcard/librarian/list_deg_prog.html'
	context_object_name = 'deg_prog'
	ordering = ['deg_name']

class DegProgStudentList(ListView):
	template_name = 'pinkcard/librarian/list_students.html'
	model = DegreeProg
	context_object_name = 'students'
	
	
	def get_queryset(self):
		self.degree_prog = get_object_or_404(DegreeProg, pk=self.kwargs['pk'])
		return Student.objects.filter( degree_prog = self.degree_prog)

class StudentDetailView(DetailView):
	model = Student

def DisplayElecUsage(request):

	deg_prog = DegreeProg.objects.all()
	students = Student.objects.all()

	no_hours = []	
	for dp in deg_prog:
		no_elec_usage = 0.0
		for stud in students:
			if stud.degree_prog == dp:
				no_elec_usage = no_elec_usage + float(stud.total_elec_usage)
		no_hours.append(no_elec_usage)		
	
	context = {
				'elec_usage_data': zip(deg_prog,no_hours)
	}
		
	return render(request, 'pinkcard/librarian/elec_usage.html', context)

class ElecUsageListView(ListView):		
	model = DegreeProg
	template_name = 'pinkcard/librarian/elec_usage.html'
	context_object_name = 'deg_prog'

	def testingonli(self):
		print('HEHE')
		self.degree_prog = get_object_or_404(DegreeProg, pk=self.kwargs['pk'])
		query_na = Student.objects.filter( degree_prog = self.degree_prog)

		print(query_na)

class StudentCreateView(CreateView):
	model = Student
	fields = ['id_no','last_name', 'first_name','degree_prog' ]

class StudentUpdateView(UpdateView):
	model = Student
	fields = ['id_no','last_name', 'first_name','degree_prog' ]

class StudentDeleteView(DeleteView):
	model = Student
	success_url = '/librarian/deg_prog/'
	print('DELETED HEHE')