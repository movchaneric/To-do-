import django_filters
from django_filters import CharFilter

from .models import *

class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'description', 'date_created','complete']