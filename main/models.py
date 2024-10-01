from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    itemName = models.CharField(max_length=255)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    itemStock = models.IntegerField(validators=[MinValueValidator(0)])
    itemImageURL = models.URLField(default='https://i.imgur.com/tGd7up6.jpeg')
    itemCategory = models.TextField()