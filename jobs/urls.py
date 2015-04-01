from django.conf.urls import patterns, url

urlpatterns = patterns('jobs.views',
	url(r'^$', 'jobs_list_view', name='jobs_list_view'),
	url(r'^(?P<slug>[\w-]+)-(?P<pk>\d+)/$', 'job_detail_view', name='job_detail_view'),
)
