from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account_Types(models.Model):
    type_name = models.TextField()

    def __str__(self):
        return self.type_name

class Related_accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(Account_Types, on_delete=models.CASCADE)

    def __int__(self):
        return self.pk
    # TODO: include account credentials