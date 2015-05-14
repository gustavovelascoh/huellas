'''
Created on May 14, 2015

@author: gustavo
'''

import django_filters
from .models import Report


class ReportFilter(django_filters.FilterSet):
    
    color = django_filters.CharFilter(lookup_type='icontains')
    breed = django_filters.CharFilter(lookup_type='icontains')
    
    
    class Meta:
        model = Report
        fields = ['city', 'zone', 'breed', 'color']
        
    def __init__(self, *args, **kwargs):
        super(ReportFilter, self).__init__(*args, **kwargs)
        self.filters['zone'].extra.update()