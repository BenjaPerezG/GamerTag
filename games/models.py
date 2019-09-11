from django.db import models
from django.contrib.auth.models import User

class account_types(models.Model):
    type_name = models.TextField()
    def __str__(self):
        return self.type_name

class user_accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(account_types, on_delete=models.CASCADE)
    account_username = models.TextField()
