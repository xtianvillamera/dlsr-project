from django.db import models

# Create your models here.


class Semester(models.Model):
	semesters = models.CharField(max_length=30)
	


	def __str__(self):
		return self.semesters

class DeptInst(models.Model):
	dept_inst = models.CharField(max_length=50)
	total_hours = models.DecimalField(decimal_places=2,max_digits=1000000,default=0)
	sems = models.ManyToManyField(Semester)

	def __str__(self):
		return self.dept_inst
		