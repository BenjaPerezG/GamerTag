from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.account_types)
admin.site.register(models.user_accounts)