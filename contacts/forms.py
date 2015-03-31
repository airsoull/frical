from django.template.loader import render_to_string
from django.forms import ModelForm

from .models import Contact
from .conf import settings


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'body',)

    def save(self, commit=True):
        contact = super(ContactForm, self).save(commit=commit)
        send_contact_email(contact)
        return contact

def send_contact_email(contact):
    to_address = settings.CONTACTS_EMAILS
    from_address = contact.email
    content = render_to_string("contacts/email_contact.txt", {'contact': contact})
    subject = render_to_string("contacts/email_contact_subject.txt", {'contact': contact})
    try:
        from mailqueue.models import MailerMessage
        msg = MailerMessage()
        msg.subject = subject
        msg.to_address = ", ".join(to_address)
        msg.from_address = from_address
        msg.content = content
        msg.app = 'Contacto'
        msg.send_mail()
    except ImportError:
        from django.core.mail import EmailMultiAlternatives
        msg = EmailMultiAlternatives(subject, content, from_address, to_address)
        msg.send()