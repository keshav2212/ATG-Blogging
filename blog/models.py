from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	articledate=models.DateField()
	title=models.CharField(max_length=1000)
	article=models.CharField(max_length=10000)
	def __str__(self):
		return self.title
# Create your models here.
