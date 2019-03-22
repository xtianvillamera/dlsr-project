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
- 3/8/19 - xtianvillamera added the 'pinkcard-LogIn' and 'pinkcard-UserDetailView'
on the path

File Creation: 2/6/19
Development Group: Group 7 - DLSR: Digital Library Services and Reservation 
Client Group: CS 192 WFWX, Librarians, and Computer Science Students
Purpose of the File: the purpose of the views.py is to return a web 
response, so that the project will have a UI. 
"""

from django.urls import path
from .views import *
from . import views

"""
Method Name: urlpatterns
Creation Date: 3/6/19
Purpose: Its purpose is to add paths for the url so that django
will know where or what webpage should it load
List of Calling Arguments: path
List of files/database tables: -----
Return value: ----
"""
urlpatterns = [
	path('', views.testing),
	path('login/', LogIn.as_view(), name='pinkcard-LogIn'),
	path('login_fail/', LogIn.as_view(), name='pinkcard-LogInFail'),
	path('student/<int:pk>/', UserDetailView.as_view(), name='pinkcard-UserDetailView'),
	path('map/',views.Map, name='pinkcard-map'),
	path('map/use', views.UseMap, name='pinkcard-usemap'),
	path('map/afteruse', views.AfterUseMap, name='pinkcard-afterusemap'),
]
