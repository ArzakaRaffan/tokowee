from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['itemName', 'itemDescription', 'itemPrice', 'itemStock', 'itemCategory', 'itemImageURL']