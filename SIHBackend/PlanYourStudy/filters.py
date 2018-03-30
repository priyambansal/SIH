from .models import Category
import django_filters

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['Field', 'Degree', 'Location' ]