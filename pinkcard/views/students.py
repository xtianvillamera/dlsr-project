"""
MIT License

Copyright (c) 2019 xtianvillamera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This is a course requirement for CS 192 Software Engineering II under 
the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of 
Computer Science, College of Engineering, University of the Philippines, 
Diliman for the AY 2018-2019”

Code History:
- 3/6/19 - xtianvillamera created the file
- 3/6/19 - xtianvillamera added the classes UserDetailView, LogIn
- 3/8/19 - xtianvillamera edited the class LogIn (added the functions get and post)
- 3/21/19 -xtianvillamera added the functions: Map, UseMap and AfterUseMap

File Creation: 3/6/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students
Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect, render
import decimal 
import time
from ..models import *
from ..forms import *

"""
Model Name: StudentSignUpView 
Creation Date: 3/6/19
Purpose: Using the DetailView as its generic view, UserDetailView displays
all of the information/detail (name, student no, remaining pink card hours, elec usage) 
of an engineering student in UPD. Take note that the purpose of this model
is almost the same with the model StudentDetailView in viewing app, without
other functions
List of Calling Arguments: DetailView
List of files/database tables: Student
Return Value: Webpage (generic view) containing the info/details of 
an engineering student
"""

"""

def StudentSignUp(request):
	if request.method == 'POST':
		form = StudentSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return render(request, 'pinkcard/home.html')
		else:
			form = StudentSignUpForm()
	return render(request, 'registration/signup_form.html')		

"""
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
		return render(self.request, 'pinkcard/home.html')


def StudentsDetailView(request):
	student_user = request.user.student
	context = {'last_name':student_user.last_name, 'first_name':student_user.first_name,
				'student_no':student_user.id_no,'degree_prog':student_user.degree_prog, 
				'rem_hours':student_user.rem_hours,'total_elec_usage':student_user.total_elec_usage}
	return render(request, 'pinkcard/students/students_detail.html', context)

"""
class StudentsDetailView(DetailView):
	template_name = 'pinkcard/students/students_detail.html'
	model = Student
	context_object_name = 'students'
	print(user.student.last_name)

"""

"""
Method Name: test
Creation Date: 3/6/19
Purpose: For testing purpose only
List of Calling Arguments: request
List of files/database tables: none
Return value: It will return a blank webpage (temporarily)
"""
def Test(request):
	#print(request.user.student.last_name)
	return render(request, 'pinkcard/home.html')

"""
Method Name: Map
Creation Date: 3/21/19
Purpose: Map will display the outlets on the libraries in Engg Lib 2
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""	
def Map(request):
	return render(request, 'pinkcard/students/map.html')

"""
Method Name: UseMap
Creation Date: 3/21/19
Purpose: Map will display the outlets on the libraries in Engg Lib 2 and
a clock, displaying the time the student has been consuming
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""	
def UseMap(request):
	if (request.user.student.rem_hours <= 0):
		return render(request, 'pinkcard/students/map.html')
	begin = time.time()
	request.session['begin'] = begin
	return render(request, 'pinkcard/students/usemap.html')

"""
Method Name: AfterUseMap
Creation Date: 3/21/19
Purpose: Map will display the outlets on the libraries in Engg Lib 2 and the
total time that the student consumed while using the outlet.
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""	
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


"""
Method Name: Transfer
Creation Date: 4/4/19
Purpose: It includes transferring and requesting of pinkcard hours
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""
def Transfer(request):
	return render(request, 'pinkcard/students/transfer.html')

id_num = 0

"""
Method Name: TransferHours
Creation Date: 3/21/19
Purpose: Will prompt the user to enter the student number of the
student he/she wants to transfer his/her pinkcard hours.
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""
def TransferHours(request):
	query = request.GET.get('student', None)
	qs = Student.objects.all()
	if query is not None:
		qs = qs.filter(id_no=query)
		context= {'first_name':qs[0].first_name, 'last_name':qs[0].last_name, 'degree_prog':qs[0].degree_prog, 'continue':"Continue?"}
		request.session['id_num'] = qs[0].id_no
		
		#print(id_num)
	else:
		context= {'first_name':"", 'last_name':"", 'degree_prog':"", 'continue':""}
		#print('wala students')
		
	template = 'pinkcard/students/transferhours.html'
	return render(request, template, context)

"""
Method Name: TransferringHours
Creation Date: 3/21/19
Purpose: Will now transfer the pinkcard hours to others.
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""
def TransferringHours(request):	
	t_hours = request.GET.get('hours')
	if t_hours is not None:
		print('HELLOOO')
		id_num=16
		print(request.session['id_num'])
		context= {'hours':""}
		if(request.user.student.rem_hours -  decimal.Decimal(t_hours) >= 0):
			request.user.student.rem_hours = request.user.student.rem_hours -  decimal.Decimal(t_hours)
			request.user.student.save()

			r_hours = Student.objects.filter(id_no=request.session['id_num'])[0].rem_hours
			print(r_hours+decimal.Decimal(t_hours))

			Student.objects.filter(id_no=request.session['id_num']).update(rem_hours=r_hours+decimal.Decimal(t_hours))
			context= {'hours':t_hours}

	else:
		context = {'hours':''}
	template = 'pinkcard/students/transferringhours.html'
	return render(request, template,context)	

"""
Method Name: RequestHours
Creation Date: 3/21/19
Purpose: Will request hours
List of Calling Arguments: request
List of files/database tables: Student
Return Value: A webpage displaying the map of outlets.
"""
def RequestHours(request):
	query = request.GET.get('student', None)
	qs = Student.objects.all()
	if query is not None:
		qs = qs.filter(id_no=query)
		context= {'first_name':qs[0].first_name, 'last_name':qs[0].last_name, 'degree_prog':qs[0].degree_prog, 'continue':"Continue?"}
		request.session['id_num'] = qs[0].id_no
		
		#print(id_num)
	else:
		context= {'first_name':"", 'last_name':"", 'degree_prog':"", 'continue':""}
		#print('wala students')
		
	template = 'pinkcard/students/requesthours.html'
	return render(request, template, context)

		
def RequestingHours(request):
	r_hours = request.GET.get('hours')
	if r_hours is not None:
		context= {'hours':r_hours}
		r_m = str(request.user.student.first_name) + " " + str(request.user.student.last_name) + " requested " + str(r_hours) + " hours to you."
		RequestMessage.objects.create(sender=request.user, recipient=Student.objects.filter(id_no=request.session['id_num'])[0].user, request_message=r_m)
	else:
		context = {'hours':''}
	template = 'pinkcard/students/requestinghours.html'
	return render(request, template, context)

def RequestMessages(request):
	template = 'pinkcard/students/requestmessages.html'
	context = {}
	context['messages'] = RequestMessage.objects.filter(recipient = request.user)
	print(context['messages'])

	return render(request, template, context)