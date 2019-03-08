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

File Creation: 3/6/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students
Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from digital_pinkcard.forms import LogInForm
from viewing.models import *

"""
Method Name: testing
Creation Date: 3/6/19
Purpose: For testing purpose only
List of Calling Arguments: request
List of files/database tables: none
Return value: It will return a blank webpage (temporarily)
"""
def testing(request):
	return render(request, 'digital_pinkcard/base.html')

"""
Model Name: UserDetailView 
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
class UserDetailView(DetailView):
	model = Student.objects.all()

"""
Model Name: LogIn
Creation Date: 3/6/19
Purpose: Using the TemplateView, LogIn will allow the students
to log-in on their accounts so that they can use the digital pink card,
and/or view their informations (remaining pink card hours, electric usage
report)
List of Calling Arguments: TemplateView
List of files/database tables: Student
Return Value: A webpage of the student.
"""	
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
