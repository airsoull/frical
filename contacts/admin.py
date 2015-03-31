from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent',)
    readonly_fields = ('name', 'email','body', 'sent',)

    def has_add_permission(self, request):
        return False
