from django.conf import settings as django_settings


class Settings(object):
    @property
    def IMAGE_SMALL_SIZE(self):
        return getattr(django_settings, 'IMAGE_SMALL_SIZE', "57x57")

    @property
    def IMAGE_ARROW(self):
        return getattr(django_settings, 'IMAGE_ARROW', "60x60")

    @property
    def IMAGE_MEDIUM_SIZE(self):
        return getattr(django_settings, 'IMAGE_MEDIUM_SIZE', "540")

    @property
    def IMAGE_LARGE_SIZE(self):
        return getattr(django_settings, 'IMAGE_LARGE_SIZE', "800")

    @property
    def IMAGE_EXTRA_LARGE_SIZE(self):
        return getattr(django_settings, 'IMAGE_EXTRA_LARGE_SIZE', "1024")


settings = Settings()
