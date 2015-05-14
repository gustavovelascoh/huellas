from django.shortcuts import render


from .models import Report
from .models import ReportImage

from django.utils import timezone

from django.views.generic.detail import DetailView

from .filtersets import ReportFilter

from django.shortcuts import render_to_response

# Create your views here.

def post_list(request):

    reports = Report.objects.all().order_by('pub_date').reverse()
    lost = reports.filter(type=0)
    found = reports.filter(type=1)
    images = ReportImage.objects.all()
    
    return render(request, 'pets/post_list.html', {'reports': reports,
                                                   'images': images,
                                                   'lost': lost,
                                                   'found': found})

class ReportDetailView(DetailView):
    
    model = Report
        
    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def report_list(request):

    f = ReportFilter(request.GET, queryset=Report.objects.all())
    return render_to_response('pets/report_list.html', {'filter': f})
