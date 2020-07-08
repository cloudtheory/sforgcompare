from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin
from compareorgs import views 
admin.autodiscover()

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth_response/$', views.oauth_response, name='oauth_response'),
    url(r'^job_status/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.job_status),
    url(r'^compare_orgs/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.compare_orgs),
    url(r'^compare_result/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.compare_results),
    url(r'^compare_result/(?P<job_id>[0-9A-Za-z_\-]+)/build_file/$', views.build_file),
    url(r'^re-run-job/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.rerunjob),
    url(r'^check_file_status/(?P<job_id>[0-9A-Za-z_\-]+)/$', views.check_file_status),
    url(r'^get_metadata/(?P<component_id>\d+)/$', views.get_metadata),
    url(r'^get_diffhtml/(?P<component_id>\d+)/$', views.get_diffhtml),
)
