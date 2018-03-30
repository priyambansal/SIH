from django.shortcuts import render
# from django.shortcuts import render
from .filters import CategoryFilter
from .models import Category

def search(request):
    category_list = Category.objects.all()
    category_filter = CategoryFilter(request.GET, queryset=category_list)
    return render(request, 'PlanYourStudy/category.html', {'filter': category_filter})
# Create your views here.
