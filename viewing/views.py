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

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
def Home(request):
	return render(request, 'viewing/base.html')

def ViewingDegProg(request):
	context = {
		'deg_prog': DegreeProg.objects.all(),
		'students': Student.objects.all()
	}

class DegProgListView(ListView):
	model = DegreeProg
	template_name = 'viewing/list_deg_prog.html'
	context_object_name = 'deg_prog'
	ordering = ['deg_name']
	
class DegProgDetailView(DetailView):
	model = Student
	template_name = 'viewing/list_students.html'
	context_object_name = 'students'

class DegProgStudentList(ListView):
	template_name = 'viewing/list_students.html'
	model = DegreeProg
	context_object_name = 'students'
	
	
	def get_queryset(self):
		self.degree_prog = get_object_or_404(DegreeProg, pk=self.kwargs['pk'])
		return Student.objects.filter( degree_prog = self.degree_prog)

class StudentDetailView(DetailView):
	model = Student

class ElecUsageListView(ListView):		
	model = DegreeProg
	template_name = 'viewing/elec_usage.html'
	context_object_name = 'deg_prog'

	