# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _

from .models import Contact
from .forms import ContactForm

class ContactFormView(CreateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self, instance=None):
        messages.success(self.request, _(u'Su Consulta Se Ha Enviado Con Éxito'))
        return reverse('contacts.views.contact_form_view')

contact_form_view = ContactFormView.as_view()