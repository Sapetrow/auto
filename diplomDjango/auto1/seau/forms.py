from django.forms import ModelForm

from .models import Auto, Client, Work, Product, Order

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ('number', 'marka', 'model', 'vin')

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('lastname', 'firstname', 'middlename', 'phone', 'adress')

class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ('cod', 'nameproduct', 'price')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('cod', 'nameproduct', 'price')

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'auto', 'work', 'product')