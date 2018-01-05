from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'', include('artist.urls')),
    url(r'^single', views.update_profile, name='update_profile'),
    url(r'^change$', views.update_profile, name='profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)