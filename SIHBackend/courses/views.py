from django.shortcuts import render

# Create your views here.

def undergraduate(request):
    return render(request,'courses/undergraduate.html')

def postgraduate(request):
    return render(request,'courses/postgraduate.html')
