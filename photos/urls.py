from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^search/', views.search_category, name = 'search_category'),
    url('location/(?P<location>\w+)',views.getLocations,name = 'location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
