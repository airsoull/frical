from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail
from django.template.loader import render_to_string

from .conf import settings
from .forms import ContactForm
from .models import Contact


class ContactViewTest(TestCase):

    def setUp(self):
        self. url = reverse('contacts.views.contact_form_view')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_post(self):
        params = {
            'name': 'foo',
            'email': 'admin@example.net',
            'body': 'Lorem ipsum dolor sit amet'
        }

        response = self.client.post(self.url, params)
        self.assertRedirects(response, self.url)

        contact = Contact.objects.get()
        self.assertEqual(params['name'], contact.name)
        self.assertEqual(params['email'], contact.email)
        self.assertEqual(params['body'], contact.body)

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        self.assertEqual(email.to, settings.CONTACTS_EMAILS)
        self.assertEqual(email.from_email, contact.email)

        self.assertEqual(email.subject, render_to_string('contacts/email_contact_subject.txt',
                                                         {'contact': contact}))
        self.assertEqual(email.body, render_to_string('contacts/email_contact.txt',
                                                      {'contact': contact}))
