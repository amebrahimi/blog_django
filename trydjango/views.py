import random
from django.http import HttpResponse


def home_view(request):
		''' 
		Take in a reqeust (Django send rquest)
		Return HTML as response (We pick to return the response)
		'''
		name = "Khers"
		number = random.randint(10, 1000)
		HTML_STRING= f"""
			<h1>Hello {name} - {number}</h1>
		"""
		return HttpResponse(HTML_STRING)