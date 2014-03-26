from django.db import models

class Fest(models.Model):
	name = models.CharField(max_length=260)
	country = models.CharField(max_length=260)
	start_date = models.DateField()

	def get_dict(self):
		return {'id': self.id, 'name': self.name, 'country': self.country, 
			'start_date': str(self.start_date)}
			