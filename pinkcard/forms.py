from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.models import User

from pinkcard.models import *

class LibrarianSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User

	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_librarian = True
		if commit:
			user.save()
		return user
		

class StudentSignUpForm(UserCreationForm):
	id_no = forms.IntegerField()
	last_name = forms.CharField()
	first_name = forms.CharField()
	degree_prog = forms.ModelChoiceField(
		queryset=DegreeProg.objects.all(),
		widget=forms.Select,
		required=True
	)
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','id_no', 'last_name', 'first_name', 'degree_prog', )
			
	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.last_name = self.cleaned_data.get('last_name')
		print(user.last_name)
		user.save()
		student = Student.objects.create(user=user)
		return user
