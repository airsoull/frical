from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from sorl.thumbnail import get_thumbnail

from .managers import JobManager, ImageManager
from .conf import settings


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
        self.name = self.name.strip().title()
        self.description = self.description.strip()

    def image(self):
        return self.images.visible().order_by('order').first()

    def get_absolute_url(self):
        return reverse('jobs.views.job_detail_view', kwargs={'slug': slugify(self.name), 'pk': self.pk})


class Image(models.Model):
    job = models.ForeignKey(Job, related_name='images')
    image = models.ImageField(_('Image'), max_length=255, upload_to='upload/jobs/images/%Y/%m/%d/', width_field='width', height_field='height')
    order = models.PositiveIntegerField(_('Order'), default=0)
    width = models.PositiveIntegerField(_('Width'), default=0, blank=True)
    height = models.PositiveIntegerField(_('Height'), default=0, blank=True)
    active = models.BooleanField(_('Active'), default=True)
    uploaded = models.DateTimeField(_('Uploaded'), auto_now_add=True)

    objects = ImageManager()

    def __unicode__(self):
        return u"%s (%s)" % (self.image, self.job.name)

    @property
    def small_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_SMALL_SIZE, crop="center")
        return im.url

    @property
    def arrow_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_ARROW, crop="center")
        return im.url

    @property
    def medium_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_MEDIUM_SIZE)
        return im.url

    @property
    def large_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_LARGE_SIZE)
        return im.url

    @property
    def extra_large_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_EXTRA_LARGE_SIZE)
        return im.url

    @property
    def original_url(self):
        return self.image.url
