from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

handler404 = 'pets.views.handler404'

urlpatterns = [
    # Examples:
    # url(r'^$', 'huellas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),    
    url(r'', include('pets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
