from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from digital_pinkcard.forms import LogInForm
from viewing.models import *

# Create your views here.
def testing(request):
	return render(request, 'digital_pinkcard/base.html')

class UserDetailView(DetailView):
	model = Student.objects.all()

class LogIn(TemplateView):
	template_name = 'digital_pinkcard/login.html'

	def get(self, request):
		form = LogInForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = LogInForm(request.POST)
		if form.is_valid():
			student_number = form.cleaned_data['student_number']
			password = form.cleaned_data['password']

		args = {'form':form, 'student_number': student_number, 'password': password}
		database = Student.objects.all()

		finding_student = False
		for student in database:
			if (student.student_no == args['student_number'] and student.pword == args['password']):
				print(type(student))	
				finding_student = True
				print(student.id,'hanna')
				return HttpResponseRedirect('/viewing/student/%s/' % student.id)
				

		if (finding_student == False):
			print('Wrong password')		

		return render(request, self.template_name, args)
