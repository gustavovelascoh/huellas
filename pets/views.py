from django.shortcuts import render
from .models import Report
from .models import ReportImage

# Create your views here.

def post_list(request):

    reports = Report.objects.all()
    images = ReportImage.objects.all()
    
    return render(request, 'pets/post_list.html', {'reports': reports, 'images': images})