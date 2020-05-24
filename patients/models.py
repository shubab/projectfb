from django.db import models


class patients_entry(models.Model):
	name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	
	

	def __str__(self):
		return self.name 

# Create your models here.
