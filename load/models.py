from django.db import models

# Create your models here.
class Load(models.Model):
    id = models.AutoField
    ip = models.IPAddressField
    business_id = models.IntegerField
    business_name = models.CharField(max_length = 50)
    load =models.IntegerField



