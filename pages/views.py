from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def projects(request):
	return render(request, 'projects.html')
