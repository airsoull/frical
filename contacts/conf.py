from django.conf import settings as django_settings


class Settings(object):
    @property
    def CONTACTS_EMAILS(self):
    	emails = map(lambda x: "%s <%s>" % x, list(django_settings.MANAGERS))
        return getattr(django_settings, 'CONTACTS_EMAILS', emails)

    @property
    def CONTACTS_DEFAULT_FROM_EMAIL(self):
        return getattr(django_settings, 'CONTACTS_DEFAULT_FROM_EMAIL', django_settings.DEFAULT_FROM_EMAIL)

settings = Settings()
