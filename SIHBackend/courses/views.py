from django.shortcuts import render

# Create your views here.

def undergraduate(request):
    return render(request,'courses/undergraduate.html')

def postgraduate(request):
    return render(request,'courses/postgraduate.html')

def ugscience(request):
	return render(request, 'courses/ugscience.html')

def technology(request):
	return render(request, 'courses/technology.html')

def arts(request):
	return render(request, 'courses/arts.html')

def architecture(request):
	return render(request, 'courses/architecture.html')

def management(request):
	return render(request, 'courses/management.html')
def commerce(request):
	return render(request, 'courses/commerce.html')
