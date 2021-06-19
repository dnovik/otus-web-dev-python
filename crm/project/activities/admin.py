from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ['id',
                    'author',
                    'created',
                    'modified',
                    'status',
                    'type',
                    'title',
                    'description',
                    'customer',
                    'contact']
