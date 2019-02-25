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
- 2/6/19 - xtianvillamera created the Home and ViewingDegProg function
- 2/7/19 - xtianvillamera created the classes DegProgStudentList, StudentDetailView, ElecUsageListView
- 2/19/19 - xtianvillamera created the classes DegProgListView, DegProgDetailView
- 2/19/19 - xtianvillamera created the classes StudentCreateView, StudentUpdateView, StudentDeleteView
- 2/21/19 - xtianvillamera updated/edited the classes StudentCreateView, StudentUpdateView, ElecUsageListView

File Creation: 2/5/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students
Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.views.generic import (ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
"""
Method Name: StudentsList
Creation Date: 2/6/19
Purpose: Its purpose is to display the list of all the students.
List of Calling Arguments: request
List of files/database tables: none
Return value: It will return a blank webpage (temporarily)
"""
def Home(request):
	return render(request, 'viewing/base.html')

"""
Method Name: ViewingDegProg
Creation Date: 2/6/19
Purpose: Its purpose is to display the list of all the students.
List of Calling Arguments: request
List of files/database tables: Student model
Return value: It will return the webpage containing the list of 
degree programs.
"""
@login_required
def ViewingDegProg(request):
	context = {
		'deg_prog': DegreeProg.objects.all(),
		'students': Student.objects.all()
	}

"""
Model Name: DegProgListView
Creation Date: 2/19/19
Purpose: Using the ListView as its generic view, DegProgListView displays the
list of all degree programs in UP College of Engineering
List of Calling Arguments: ListView
List of files/database tables: DegreeProg
Return Value: Webpage (generic view) containing the list 
of the degree programs in Engineering
"""
class DegProgListView(ListView):
	model = DegreeProg
	template_name = 'viewing/list_deg_prog.html'
	context_object_name = 'deg_prog'
	ordering = ['deg_name']

"""
Model Name: DegProgStudentList 
Creation Date: 2/7/19
Purpose: Using the ListView as its generic view, DegProgStudentList displays all
of the students in a certain engineering course
List of Calling Arguments: ListView
List of files/database tables: DegreeProg, Student
Return Value: Webpage (generic view) containing the students
of a certain engineering course
"""
class DegProgStudentList(ListView):
	template_name = 'viewing/list_students.html'
	model = DegreeProg
	context_object_name = 'students'
	
	
	def get_queryset(self):
		self.degree_prog = get_object_or_404(DegreeProg, pk=self.kwargs['pk'])
		return Student.objects.filter( degree_prog = self.degree_prog)

"""
Model Name: StudentDetailView 
Creation Date: 2/7/19
Purpose: Using the DetailView as its generic view, StudentDetailView displays
all of the information/detail (name, student no, remaining pink card hours, elec usage) 
of an engineering student in UPD
List of Calling Arguments: DetailView
List of files/database tables: Student
Return Value: Webpage (generic view) containing the info/details of 
an engineering student
"""
class StudentDetailView(DetailView):
	model = Student

"""
Model Name: ElecUsageListView
Creation Date: 2/7/19
Purpose: Using the ListView as its generic view, ElecUsageListView displays
the electric usage per degree program in the UPD College of Engineering
List of Calling Arguments: ListView
List of files/database tables: DegreeProg
Return Value: Webpage (generic view) containing the electric usage per
degree program in the UPD College of Engineering
"""

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
		
	return render(request, 'viewing/elec_usage.html', context)

class ElecUsageListView(ListView):		
	model = DegreeProg
	template_name = 'viewing/elec_usage.html'
	context_object_name = 'deg_prog'

	def testingonli(self):
		print('HEHE')
		self.degree_prog = get_object_or_404(DegreeProg, pk=self.kwargs['pk'])
		query_na = Student.objects.filter( degree_prog = self.degree_prog)

		print(query_na)	
"""
Model Name: StudentCreateView
Creation Date: 2/19/19
Purpose: Using the CreateView as its generic view, StudentCreateView
can add another student on the database
List of Calling Arguments: CreateView
List of files/database tables: Student 
Return Value: Webpage (generic view) containing the form that will
add another student in the database
"""
class StudentCreateView(CreateView):
	model = Student
	fields = ['student_no','last_name', 'first_name','degree_prog' ]

"""
Model Name: StudentUpdateView
Creation Date: 2/19/19
Purpose: Using the UpdateView as its generic view, StudentUpdateView
can update certain information of the student
List of Calling Arguments: UpdateView
List of files/database tables: Student 
Return Value: Webpage (generic view) containing the form that will
update some information of the student
"""
class StudentUpdateView(UpdateView):
	model = Student
	fields = ['student_no','last_name', 'first_name','degree_prog' ]

"""
Model Name: StudentDeleteView
Creation Date: 2/19/19
Purpose: Using the DeleteView as its generic view, StudentDeleteView
can remove students on the database
List of Calling Arguments: DeleteView
List of files/database tables: Student
Return Value: Webpage (generic view) containing the form that will
ask if you are sure that you will remove that student in the
database
"""
class StudentDeleteView(DeleteView):
	model = Student
	success_url = '/viewing/deg_prog/'
	print('DELETED HEHE')