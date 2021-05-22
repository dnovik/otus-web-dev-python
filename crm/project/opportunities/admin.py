from django.contrib import admin
from .models import Opportunity


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ['title',
                    'account',
                    'contact',
                    'created',
                    'modified',
                    'activities']
