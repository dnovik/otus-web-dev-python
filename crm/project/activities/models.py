from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Account
from contacts.models import Contact


class Activity(models.Model):

    class Status(models.TextChoices):
        INACTIVE = 'Inactive'
        OPEN = 'Open'
        IN_PROGRESS = 'In progress'

    author = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Status.choices, default=Status.OPEN, max_length=12)
    short_description = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    customer = models.ForeignKey(Account, on_delete=models.PROTECT)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)

    def __str__(self):
        return self.short_description