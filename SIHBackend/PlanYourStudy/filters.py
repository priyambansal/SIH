from .models import Category
import django_filters

class CategoryFilter(django_filters.FilterSet):
    Field=django_filters.CharFilter()
    Degree=django_filters.CharFilter()
    Address=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Category
        fields = ['Field', 'Degree', 'Address' ]
