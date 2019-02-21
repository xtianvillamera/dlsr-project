from django.db import models
from django.urls import reverse

# Create your models here.
class DegreeProg(models.Model):
	deg_name = models.CharField(max_length=200,default='Non Major')

	def __str__(self):
		return self.deg_name

	class Meta:
		ordering = ('deg_name',)	

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

class Semester(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	degree_prog = models.ForeignKey(DegreeProg, on_delete=models.CASCADE)
	sem = models.CharField(max_length=50)

	def __str__(self):
		return self.sem