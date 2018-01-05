from django.conf.urls import url

from . import views
app_name = 'artist'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^gallery.html$', views.gallery, name='gallery'),
    url(r'^services.html$', views.services, name='services'),
    url(r'^single.html$', views.single, name='single'),
    url(r'^typo.html$', views.typo, name='typo'),
    url(r'^index1.html$', views.ttt, name='ttt'),
]