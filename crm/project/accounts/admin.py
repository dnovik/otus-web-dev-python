from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ['id', 'name', 'created', 'modified', 'email', 'phone']