from django.db import models

class User_(models.Model):
    question_text = models.CharField(max_length=200)
