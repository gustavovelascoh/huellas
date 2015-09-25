'''
Created on May 14, 2015

@author: gustavo
'''

import django_filters
from .models import Report
from django_filters.filterset import ORDER_BY_FIELD


class ReportFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(lookup_type='icontains')
    name.label = 'Nombre'
    
    color = django_filters.CharFilter(lookup_type='icontains')
    
    breed = django_filters.CharFilter(lookup_type='icontains')
    breed.label = 'Raza'
    
    city = django_filters.CharFilter(lookup_type='icontains')
    city.label = 'Ciudad'
    
    zone = django_filters.ChoiceFilter(choices=Report.ZONE_CHOICES)
    zone.label='Zona'
    
    genre = django_filters.ChoiceFilter(choices=Report.GENRE_CHOICES)
    genre.label='Género'
    
    
    
    class Meta:
        model = Report
        fields = ['name', 'city', 'zone', 'breed', 'genre', 'color']
        order_by = ['-pub_date']
        order_by_field = "-pub_date"
        
        
    def __init__(self, *args, **kwargs):
        super(ReportFilter, self).__init__(*args, **kwargs)
        self.filters['zone'].extra.update(
                                          #{'label': 'Zona'},                                          
                                         )