from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

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


class JobDetailView(TestCase):

	def setUp(self):
		self.job = Job.objects.create(name='foo', description='bar', active=True)
		self.url = reverse('jobs.views.job_detail_view', kwargs={'slug': slugify(self.job.name), 'pk': self.job.pk})

	def test_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)

		self.assertTemplateUsed('jobs/job_detail.html')
		self.assertEqual(self.job, response.context['object'])

	def test_no_active(self):
		self.job.active = False
		self.job.save()

		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 404)
		self.assertTemplateUsed('404.html')
