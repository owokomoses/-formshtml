from __future__ import unicode_literals
from django.db import models


class students(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=35)
    DOB = models.CharField(date_time=8)

    class Meta:
        db_table = "students"
