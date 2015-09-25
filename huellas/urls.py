from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from pets import views

handler404 = 'pets.views.handler404'


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reports', views.ReportViewSet)
router.register(r'reportimages', views.ReportImageViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'huellas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),    
    url(r'', include('pets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
