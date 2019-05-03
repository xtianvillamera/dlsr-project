from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.core.validators import MinLengthValidator

# Create your models here.

class User(AbstractUser):
	username = models.CharField(max_length=30, unique=True)
	is_student = models.BooleanField(default=False)
	is_librarian = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'

class DegreeProg(models.Model):
	deg_name = models.CharField(max_length=200, default='Non Major')

	def __str__(self):
		return self.deg_name

	class Meta:
		ordering = ('deg_name',)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	id_no = models.IntegerField(null=True)
	last_name = models.CharField(max_length = 30, default="Doe")
	first_name = models.CharField(max_length = 30, default="Jane")
	degree_prog = models.ForeignKey(DegreeProg, null=True, blank=True,on_delete=models.CASCADE)
	rem_hours = models.DecimalField(decimal_places=2,max_digits=1000,default=20.0)
	total_elec_usage = models.DecimalField(decimal_places=2,max_digits=1000,default=0)
	
	
	def __str__(self):
		return self.last_name

class RequestMessage(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender_notification')
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_notification')
	request_message = models.TextField()
	sent_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.request_message		