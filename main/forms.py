from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['itemName', 'itemDescription', 'itemPrice', 'itemStock', 'itemCategory', 'itemImageURL']

    def clean_itemName(self):
        itemName = self.cleaned_data["itemName"]
        return strip_tags(itemName)
    
    def clean_itemDescription(self):
        itemDescription = self.cleaned_data["itemDescription"]
        return strip_tags(itemDescription)
    
    def clean_itemPrice(self):
        itemPrice = self.cleaned_data["itemPrice"]
        return strip_tags(itemPrice)
    
    def clean_itemStock(self):
        itemStock = self.cleaned_data["itemStock"]
        return strip_tags(itemStock)
    
    def clean_itemCategory(self):
        itemCategory = self.cleaned_data["itemCategory"]
        return strip_tags(itemCategory)
    
    def clean_itemImageURL(self):
        itemImageURL = self.cleaned_data["itemImageURL"]
        return strip_tags(itemImageURL)
