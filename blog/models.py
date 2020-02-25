from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	articledate=models.DateField()
	title=models.CharField(max_length=1000)
	Description=models.CharField(max_length=10000)
	Image=models.ImageField(upload_to="article_image",blank=False)
	def __str__(self):
		return self.title
# Create your models here.
