from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
	template_name = 'registration/signup.html'


def home(request):
	if request.user.is_authenticated:
		if request.user.is_librarian:
			return redirect('librarian')
		else:
			return redirect('students:test')
	return render(request, 'pinkcard/home.html')