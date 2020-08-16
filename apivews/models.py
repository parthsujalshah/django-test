from django.db import models


class Temp(models.Model):
    temp_field = models.CharField(max_length=5)