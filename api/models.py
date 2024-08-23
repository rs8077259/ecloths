from django.db import models

# Create your models here.

class MenWear(models.Model):
    db_table = "menwear"
    url = models.URLField(max_length=200 ,null=True)
    title = models.CharField(max_length=80,null=True)
    price = models.CharField(max_length=4,null=True)
    mrp = models.CharField(max_length=4,null=True)
    image_link = models.URLField(max_length=200,null=True)
    last_7_day_sale = models.IntegerField(null=True)
    fit = models.CharField(max_length=50,null=True)
    fabric = models.CharField(max_length=50,null=True)
    neck = models.CharField(max_length=20,null=True)
    sleeve = models.CharField(max_length=50,null=True)
    pattern = models.CharField(max_length=50,null=True)
    length = models.CharField(max_length=40,null=True)
    description = models.TextField(max_length=400,null=True)
    links = models.JSONField(null=True)
    available_skus = models.JSONField(null=True)




