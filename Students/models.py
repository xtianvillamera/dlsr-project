from django.db import models

# Create your models here.
class Student(models.Model):
	last_name = models.CharField(max_length = 30)
	first_name = models.CharField(max_length = 30)
	degree_prog = models.CharField(max_length = 50)
	student_no = models.IntegerField()
	rem_hours = models.DecimalField(decimal_places=2,max_digits=1000,default=20.0)
	total_elec_usage = models.DecimalField(decimal_places=2,max_digits=1000,default=0)

	def __str__(self):
		return self.last_name	