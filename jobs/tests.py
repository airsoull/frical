from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Job


class JobsListView(TestCase):

	def setUp(self):
		self.url = reverse('jobs.views.jobs_list_view')

	def test_get(self):
		job1 = Job.objects.create(name='foo', description='bar', active=True)
		job2 = Job.objects.create(name='foo', description='bar', active=False)

		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_list.html')

		self.assertIn(job1, response.context['job_list'])
		self.assertNotIn(job2, response.context['job_list'])
