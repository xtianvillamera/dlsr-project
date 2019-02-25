from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testing(request):
	return render(request, 'digital_pinkcard/base.html')

def login(request):
	return render(request, 'digital_pinkcard/login.html')	