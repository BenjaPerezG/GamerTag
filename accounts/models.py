from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=32)
    email = models.EmailField()

class Account_Types(models.Model):
    type_name = models.TextField()

class Related_accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(Account_Types, on_delete=models.CASCADE)
    # TODO: include account credentials