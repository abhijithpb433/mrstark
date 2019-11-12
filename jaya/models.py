from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.IntegerField(max_length=3)
    offer = models.BooleanField(default=False)
    dimensions = models.CharField(max_length=300,null=True,blank=True)
    image = models.ImageField(upload_to='pics')
    # def __str__(self):
    #     return self.title