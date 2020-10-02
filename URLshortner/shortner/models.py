from django.db import models

class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=4095)
    short_link = models.CharField(max_length=128)
