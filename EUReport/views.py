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
- 2/6/19 - xtianvillamera created the EURHome function and ReportListView class
- 2/7/19 - xtianvillamera edited the EURHome function and ReportListView class

File Creation: 2/6/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students

Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Semester, DeptInst

# Create your views here.
"""
Method Name: EURHome
Creation Date: 2/6/19
Purpose: Its purpose is to display the list of electric usage report per department/institute/degree program.
List of Calling Arguments: request
List of files/database tables: Semester, DeptInst model
Return value: It will return the webpage containing the list of 
electric usage report.
"""
def EURHome(request):
	context = {
		'deptsinsts': DeptInst.objects.all(),
		'sems': Semester.objects.all()
	}
	return render(request,'EUReport/EURPage.html')

"""
Method Name: ReportListView
Creation Date: 2/6/19
Purpose: Its purpose is to display the list of electric usage report per department/institute/degree program,
using the ListView object
List of Calling Arguments: ListView
List of files/database tables: Semester, DeptInst model
Return value: It will return the webpage containing the list of 
electric usage report.
"""
class ReportListView(ListView):
	model = DeptInst
	template_name = 'EUReport/EURPage.html'
	context_object_name = 'deptsinsts'
