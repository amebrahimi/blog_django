import random
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article

def home_view(request):
		''' 
		Take in a reqeust (Django send rquest)
		Return HTML as response (We pick to return the response) ''' 
		article_obj = Article.objects.get(id=random.randint(1,2)) 
		article_queryset = Article.objects.all()

		context = {
			"title": article_obj.title,
			"content": article_obj.content,
			"id": article_obj.id,
			"object_list": article_queryset
		}

		HTML_STRING = render_to_string("home-view.html", context=context)

		return HttpResponse(HTML_STRING)