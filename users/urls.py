from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^change/', views.update_profile, name='update_profile'),
    url(r'^works/', views.works_new, name='works_new'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='post_detail'),

    url(r'^single.html$', views.post_new, name='post_new'),
    url(r'^typoshow.html', views.posting_work, name='posting_work'),
    url(r'^work/(?P<pk>[0-9]+)/$', views.work_detail2,name='work_detail2'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^typo.html', views.IndexView.as_view(), name='posting'),
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^delbook/$',views.post_delete),
    url(r'^delwork/$',views.work_delete),
    url(r'^editorbook/(\d+)',views.post_edit),
   # url(r'^services.html$', views.list, name='list'),
    url(r'^services.html', views.admin_posting, name='admin_posting'),
    url(r'^post123/(?P<pk>[0-9]+)/$', views.admin_post_detail,name='admin_post_detail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


