from django.contrib import admin
from .models import AccountItem


@admin.register(AccountItem)
class AccountAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ['id', 'name', 'created', 'modified', 'email', 'phone']