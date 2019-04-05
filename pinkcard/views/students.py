from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
import decimal 
import time
from ..models import *
from ..forms import *

class StudentSignUpView(CreateView):
	model = User
	form_class = StudentSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)
	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return render(request, 'pinkcard/home.html')

class StudentsDetailView(DetailView):
	template_name = 'pinkcard/students/students_detail.html'
	model = Student
	context_object_name = 'students'

def Test(request):
	return render(request, 'pinkcard/students/map.html')

def Map(request):
	return render(request, 'pinkcard/students/map.html')

def UseMap(request):
	if (request.user.student.rem_hours <= 0):
		return render(request, 'pinkcard/students/map.html')
	begin = time.time()
	request.session['begin'] = begin
	return render(request, 'pinkcard/students/usemap.html')

def AfterUseMap(request):
	end = decimal.Decimal(time.time())
	duration = decimal.Decimal(end - decimal.Decimal(request.session.get('begin')))
	request.user.student.rem_hours = request.user.student.rem_hours - (duration/(decimal.Decimal(60.0)))
	request.user.student.save()
	request.user.student.total_elec_usage = request.user.student.total_elec_usage + (duration/decimal.Decimal(60.0))
	request.user.student.save()
	context = {}
	context['duration'] = duration
	return render(request, 'pinkcard/students/afterusemap.html',context)
 
def Transfer(request):
	return render(request, 'pinkcard/students/transfer.html')

id_num = 0
def TransferHours(request):
	query = request.GET.get('student', None)
	qs = Student.objects.all()
	if query is not None:
		qs = qs.filter(id_no=query)
		context= {'first_name':qs[0].first_name, 'last_name':qs[0].last_name, 'degree_prog':qs[0].degree_prog, 'continue':"Continue?"}
		id_num = qs[0].id_no
		
		print(id_num)
	else:
		context= {'first_name':"", 'last_name':"", 'degree_prog':"", 'continue':""}
	template = 'pinkcard/students/transferhours.html'
	return render(request, template, context)

def TransferringHours(request):	
	t_hours = request.GET.get('hours')
	if t_hours is not None:
		print('HELLOOO')
		id_num=16
		context= {'hours':""}
		if(request.user.student.rem_hours -  decimal.Decimal(t_hours) >= 0):
			request.user.student.rem_hours = request.user.student.rem_hours -  decimal.Decimal(t_hours)
			request.user.student.save()

			r_hours = Student.objects.filter(id_no=id_num)[0].rem_hours
			print(r_hours+decimal.Decimal(t_hours))

			Student.objects.filter(id_no=id_num).update(rem_hours=r_hours+decimal.Decimal(t_hours))
			context= {'hours':t_hours}

	else:
		context = {'hours':''}
	template = 'pinkcard/students/transferringhours.html'
	return render(request, template,context)	

def RequestHours(request):
	t_hours = request.GET.get('number')
	if t_hours is not None:
		context = {'text':"You have requested 8 hours from Sherri Vermouth"}
	else:
		context = {'text':""}
	template = 'pinkcard/students/requesthours.html'
	return render(request, template,context)	