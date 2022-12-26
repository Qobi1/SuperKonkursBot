from django.db import models

# Create your models here.


class Data(models.Model):
    user_id = models.BigIntegerField(null=True)
    language = models.CharField(max_length=256, null=True)
    state = models.IntegerField(null=True)
    contact = models.CharField(max_length=256)
    invited_by = models.BigIntegerField(null=True)
    message = models.BooleanField(default=False)
