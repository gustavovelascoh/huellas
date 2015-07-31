from django import forms

from .models import Report
from .models import ReportImage

class ReportImageCreateForm(forms.ModelForm):
    
    #images = forms.FileInput()
    #name = forms.CharField(max_length=100)
    class Meta:
        model = ReportImage
        fields = '__all__'
        #fields = ['type', 'name', 'animal', 'breed', 'color',
                  #'city', 'genre', 'zone', 'n_hood', 'email', 'phone']#, 'reportimage_set']
    pass

class ReportCreateForm(forms.ModelForm):
    
    #images = forms.FileInput()
    #name = forms.CharField(max_length=100)
    #reportimage_set = forms.ImageField()
    
    class Meta:
        model = Report
        fields = ('type', 'animal', 'name', 'breed', 'color', 'genre',
                  'city',  'zone', 'n_hood', 
                  'comment', 'email', 'phone')
    pass

