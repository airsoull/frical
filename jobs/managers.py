from django.db import models

class JobManager(models.Manager):
	use_for_related_fields = True

	def visible(self):
		return self.get_query_set().filter(active=True)
	visible.queryset_method = True


class ImageManager(models.Manager):
	use_for_related_fields = True

	def visible(self):
		return self.get_query_set().filter(active=True)
	visible.queryset_method = True
