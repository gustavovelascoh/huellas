from django.conf.urls import include, url
from . import views

from .models import Report

from django_filters.views import  FilterView

urlpatterns = [
    url(r'report/(?P<pk>[-\w]+)/$', views.ReportDetailView.as_view(), name='report-detail'),
    url(r'report/create$', views.ReportCreateView.as_view(), name='report-create'),
    url(r'reportimage/create$', views.ReportImageCreateView.as_view(), name='report-create'),
    url(r'^listG$', FilterView.as_view(model=Report)),
    url(r'^list$', views.report_list),
    url(r'^$', views.post_list),
]

