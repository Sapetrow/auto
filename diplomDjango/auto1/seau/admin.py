from django.contrib import admin

# Register your models here.
from .models import Auto, Client, Product, Work, Order


class AutoAdmin(admin.ModelAdmin):
    list_display = ('number', 'marka', 'model', 'vin')
    list_display_links = ('number', 'marka')
    search_fields = ('number', 'vin')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'middlename', 'phone', 'adress')
    list_display_links = ('lastname', 'firstname')
    search_fields = ('lastname', 'phone')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod', 'nameproduct', 'price')
    list_display_links = ('cod','nameproduct')
    search_fields = ('cod', 'nameproduct')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('cod', 'nameproduct', 'price')
    list_display_links = ('cod','nameproduct')
    search_fields = ('cod', 'nameproduct')





admin.site.register(Auto, AutoAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Order)

