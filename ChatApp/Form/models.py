from django.db import models

class Logger(models.Model):
    nickname = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
