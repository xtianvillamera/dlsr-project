from django import forms


class LogInForm(forms.Form):
	student_number = forms.IntegerField()
	password = forms.CharField(widget=forms.PasswordInput())
	