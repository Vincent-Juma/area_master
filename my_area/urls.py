from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^new/profile$', views.add_profile, name='edit'),
    url(r'^myprofile$',views.my_profile,name ='myprofile'),
    url('^addmy_area',views.addmy_area,name='addmy_area'),
    url(r'^detail/(?P<myloc_id>\d+)/$',views.myloc_details, name='detail'),
    url(r'^new_activity/(?P<pk>\d+)/$' , views.new_activity,name='new_activity'),
    url(r'^new_post/(?P<pk>\d+)$', views.new_post,name='new_post'),
    url(r'^search/$', views.search_project, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)