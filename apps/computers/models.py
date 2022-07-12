from django.db import models


class ComputerModel(models.Model):
	class Meta:
		db_table = 'computers'
	brand = models.CharField(max_length=25)
	model = models.CharField(max_length=25)
	ram = models.IntegerField()
	monitor = models.IntegerField()
