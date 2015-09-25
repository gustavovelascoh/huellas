'''
Created on Jul 9, 2015

@author: Gustavo Velasco-Hernandez
'''
from rest_framework import serializers

from pets.models import Report, ReportImage


class ReportImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportImage
        fields = ('image',)

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    reportimage_set = ReportImageSerializer(many=True)
    class Meta:
        model = Report
        fields = ('name', 'animal', 'breed', 'color', 'city', 'genre',
                   'zone', 'n_hood', 'comment', 'type', 'pub_date', 'reportimage_set')

