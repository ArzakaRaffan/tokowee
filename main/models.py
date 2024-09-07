from django.db import models

class Product(models.Model):
    itemName = models.CharField(max_length=255)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    itemStock = models.IntegerField(max_length=999)
    itemCategory = models.TextField()
    itemUploaded = models.TimeField(auto_now_add=True)