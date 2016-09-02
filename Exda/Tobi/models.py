from django.db import models
from django.conf import settings

class mydb(models.Model):
	id = models.IntegerField(default=0, primary_key=True)
	n_of_requests = models.IntegerField(default=0)
