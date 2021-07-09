from django.db import models
from accounts.models import AccountItem


class Contact(models.Model):

    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_num = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.ForeignKey(AccountItem, on_delete=models.CASCADE, related_name='contacts')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
