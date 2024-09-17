from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    itemName = models.CharField(max_length=255)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    itemStock = models.IntegerField()
    itemImageURL = models.URLField(default='https://i.imgur.com/tGd7up6.jpeg')
    itemCategory = models.TextField()