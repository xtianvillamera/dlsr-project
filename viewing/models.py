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
- 2/6/19 - xtianvillamera added models DegreeProg, Student, Semester

File Creation: 2/6/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students
Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""

from django.db import models
from django.urls import reverse

# Create your models here.

"""
Model Name: DegreeProg
Creation Date: 2/6/19
Purpose: It is a model for the degree programs in UPD College of Engineering
List of Calling Arguments: models.Model
List of files/database tables: -----
Return value: the model itself
"""
class DegreeProg(models.Model):
	deg_name = models.CharField(max_length=200,default='Non Major')

	def __str__(self):
		return self.deg_name

	class Meta:
		ordering = ('deg_name',)	

"""
Model Name: Student
Creation Date: 2/6/19
Purpose: It is a model for the UPD College of Engineering students
List of Calling Arguments: models.Model
List of files/database tables: -----
Return value: the model itself
"""
class Student(models.Model):
	last_name = models.CharField(max_length = 30)
	first_name = models.CharField(max_length = 30)
	degree_prog = models.ForeignKey(DegreeProg, on_delete=models.CASCADE)
	student_no = models.IntegerField()
	rem_hours = models.DecimalField(decimal_places=2,max_digits=1000,default=20.0)
	total_elec_usage = models.DecimalField(decimal_places=2,max_digits=1000,default=0)

	def __str__(self):
		return self.last_name

	def get_absolute_url(self):
		return reverse('viewing-StudentDetailView', kwargs={'pk': self.pk})	

"""
Model Name: Semester
Creation Date: 2/6/19
Purpose: It is a model for the semesters occured
List of Calling Arguments: models.Model
List of files/database tables: -----
Return value: the model itself
"""
class Semester(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	degree_prog = models.ForeignKey(DegreeProg, on_delete=models.CASCADE)
	sem = models.CharField(max_length=50)

	def __str__(self):
		return self.sem