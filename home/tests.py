from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeView(TestCase):

	def setUp(self):
		self.url = reverse('home.views.home')

	def test_get(self):
		response = self.client.get(self.url)
		self.assertEqual(200, response.status_code)
		self.assertTemplateUsed(response, 'home/home.html')
