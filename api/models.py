from django.db import models

# Create your models here.
class US_male_name(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

class US_female_name(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

class US_last_name(models.Model):
    last_name = models.CharField(primary_key=True,max_length=20)