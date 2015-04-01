from django.contrib import admin

from .models import Job, Image


class ImageAdminInline(admin.TabularInline):
	model = Image
	readonly_fields = ('width', 'height', 'uploaded',)
	list_editable = ('order', 'active',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	list_display = ('name', 'order', 'active',)
	list_filter = ('active',)
	list_editable = ('order', 'active',)

	inlines = [ImageAdminInline,]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('job', 'order', 'active')
