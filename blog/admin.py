from django.contrib import admin
from .models import Article
class ArticleAdmin(admin.ModelAdmin):
	list_display=['user','Description','articledate']
admin.site.register(Article,ArticleAdmin)
# Register your models here.
