from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

from .managers import JobManager, ImageManager


class Job(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    description = models.TextField(_('Description'))
    order = models.PositiveIntegerField(_('Order'), default=0)
    active = models.BooleanField(_('Active'), default=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    objects = JobManager()

    def __unicode__(self):
        return '%s' % (self.name)

    def clean(self):
        self.name = self.name.strip().lower()
        self.description = self.description.strip()

    @property
    def image(self):
        key = self.get_image_cache_key()
        image = cache.get(key)
        if not image:
            image = self.images.all()[0] if self.images.count() else None
            cache.set(key, image)
        return image

    def get_image_cache_key(self):
        return 'job.%d.image' % self.id


class Image(models.Model):
    job = models.ForeignKey(Job, related_name='jobs')
    image = models.ImageField(_('Image'), max_length=255, upload_to='upload/jobs/images/%Y/%m/%d/', width_field='width', height_field='height')
    order = models.PositiveIntegerField(_('Order'), default=0)
    width = models.PositiveIntegerField(_('Width'), default=0, blank=True)
    height = models.PositiveIntegerField(_('Height'), default=0, blank=True)
    active = models.BooleanField(_('Active'), default=True)
    uploaded = models.DateTimeField(_('Uploaded'), auto_now_add=True)

    objects = ImageManager()

    def __unicode__(self):
        return u"%s (%s)" % (self.image, self.job.name)

    def get_absolute_url(self):
        return self.image.url
