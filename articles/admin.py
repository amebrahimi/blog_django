from django.contrib import admin

# Register your models here.
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'slug', 'created_at', 'updated_at']
	search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)