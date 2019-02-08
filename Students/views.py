from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Student

# Create your views here.
def StudentsList(request):
	context = {
		'students': Student.objects.all()
	}
	for i in context['students']:
		i.rem_hours = i.rem_hours/60.0
		i.rem_hours = round(i.rem_hours, 2)
		print(i.rem_hours)
	return render(request, 'Students/ListStudents.html',context)

class StudentListView(ListView):

	model = Student
	template_name = 'Students/ListStudents.html'
	context_object_name = 'students'
	ordering = ['last_name']

class StudentDetailView(DetailView):
	model = Student	 