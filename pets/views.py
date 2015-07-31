from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.utils import timezone
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory

from .models import Report
from .models import ReportImage
from .filtersets import ReportFilter
from .serializers import ReportSerializer, ReportImageSerializer
from .forms import ReportCreateForm, ReportImageCreateForm

from rest_framework import viewsets


# Create your views here.

def post_list(request):

    reports = Report.objects.all().order_by('pub_date').reverse()
    lost = reports.filter(type=0)[:3]
    found = reports.exclude(type=0)[:3]
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
    return render_to_response('pets/report_list.html', {'filter': f, 'user': request.user})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ReportImage.objects.all()
    serializer_class = ReportImageSerializer
        
       
class ReportImageCreateView(CreateView):
    
    model = ReportImage
    
    #fields = ['type', 'name', 'animal', 'breed', 'color',
    #'city', 'genre', 'zone', 'n_hood', 'email', 'phone', 'reportimage_set']
    ReportImageFormSet = modelformset_factory(ReportImage, fields=('image',))
    
    form_class = ReportImageCreateForm
    
    formset = ReportImageFormSet(queryset=ReportImage.objects.none())
    
    def render_to_response(self, context, **response_kwargs):
        context["formset"] = self.formset
        return CreateView.render_to_response(self, context, **response_kwargs)
    
    def post(self, request, *args, **kwargs):
        
        print(request.POST)
        print(request.FILES)
        
        iform = ReportImageCreateForm(request.POST, request.FILES)
        
        print(iform)
        
        return CreateView.post(self, request, *args, **kwargs)

class ReportCreateView(CreateView):
    
    model = Report
    
    #fields = ['type', 'name', 'animal', 'breed', 'color',
    #'city', 'genre', 'zone', 'n_hood', 'email', 'phone', 'reportimage_set']
    
    form_class = ReportCreateForm
    
    def post(self, request, *args, **kwargs):
        
        print(request.POST)
        
        form = ReportImageCreateForm(request.POST)
        
        print(form)
        
        return CreateView.post(self, request, *args, **kwargs)
      
    