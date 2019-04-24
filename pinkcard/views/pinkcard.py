from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def SignUpView(request):
	return render(request, 'registration/signup.html')

def home(request):
	if request.user.is_authenticated:
		if request.user.is_librarian:
			return redirect('librarian:home')
		else:
			return redirect('students:test')
	return render(request, 'pinkcard/home.html')