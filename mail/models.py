from django.db import models


# Create your models here.

class Mail(models.Model):
    email = models.EmailField(unique=False, verbose_name="Email")
    text = models.TextField(verbose_name="Text")

