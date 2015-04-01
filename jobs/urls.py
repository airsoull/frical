from django.conf.urls import patterns, url

urlpatterns = patterns('jobs.views',
	url(r'^$', 'jobs_list_view', name='jobs_list_view'),
)
