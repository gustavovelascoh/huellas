from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'(?P<pk>[-\w]+)/$', views.ReportDetailView.as_view(), name='report-detail'),
    url(r'^$', views.post_list),
]