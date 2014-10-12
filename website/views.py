from django.shortcuts import render

def home(request):

	return render(request, "themes/bliss/index.html", {})
