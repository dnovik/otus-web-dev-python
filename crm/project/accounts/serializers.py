from rest_framework import serializers
from .models import AccountItem


class AccountItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountItem
        fields = 'name', 'created', 'modified', 'email', 'phone'
        view_name = 'account_item'
