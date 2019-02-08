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
- 2/6/19 - xtianvillamera created the StudentsList function
- 2/7/19 - xtianvillamera created the classes StudentsListView and StudentDetailView

File Creation: 2/5/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students
Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Student

# Create your views here.
"""
Method Name: StudentsList
Creation Date: 2/6/19
Purpose: Its purpose is to display the list of all the students.
List of Calling Arguments: request
List of files/database tables: Student model
Return value: It will return the webpage containing the list of 
students.
"""
def StudentsList(request):
	context = {
		'students': Student.objects.all()
	}
	
	return render(request, 'Students/ListStudents.html',context)

"""
Method Name: StudentListView
Creation Date: 2/7/19
Purpose: Its purpose is to display the list of all the students,
the same with the StudentsList function but it used the
class of ListView, as a generic way of view.
List of Calling Arguments: ListView object
List of files/database tables: Student model
Return value: It will return the webpage containing the list of 
students
"""
class StudentListView(ListView):

	model = Student
	template_name = 'Students/ListStudents.html'
	context_object_name = 'students'
	ordering = ['last_name']

"""
Method Name: StudentDetailView
Creation Date: 2/8/19
Purpose: Its purpose is to display the detailed view per student
List of Calling Arguments: DetailView object
List of files/database tables: Student model
Return value: It will return the webpage containing the list of 
students
"""
class StudentDetailView(DetailView):
	model = Student	 
