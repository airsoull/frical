from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class Config(models.Model):
	site = models.OneToOneField(Site, related_name='config')
	description = models.CharField(_('Description'), max_length=150)
	address = models.CharField(_('Address'), max_length=50)
	phone = models.CharField(_('Phone'), max_length=50)

	def __unicode__(self):
		return self.site.name

	def clean(self):
		self.description = self.description.strip()
		self.address = self.address.strip()
		self.phone = self.phone.strip()