from django.db import models
from accounts.models import AccountItem
from contacts.models import Contact
from activities.models import Activity


class Opportunity(models.Model):

    title = models.CharField(max_length=200, null=False)
    account = models.ForeignKey(AccountItem, on_delete=models.PROTECT)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    activities = models.ForeignKey(Activity, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
