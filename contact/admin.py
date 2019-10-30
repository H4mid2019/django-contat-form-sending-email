from django.contrib import admin
from .models import Contact, EmailSetting


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(EmailSetting)
class EmailSettingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'from_email')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
