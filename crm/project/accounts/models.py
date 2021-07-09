from django.db import models


class AccountItem(models.Model):

    name = models.CharField(max_length=150, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


