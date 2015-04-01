# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_('Name'), max_length=60)
    email = models.EmailField(_('Email'), max_length=50)
    body = models.TextField(_('Body'))
    sent = models.DateTimeField(_('Sent'), auto_now_add=True)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.email)

    def clean(self):
    	self.name = self.name.strip().title()
        self.email = self.email.strip().lower()
        self.body = self.body.strip()
