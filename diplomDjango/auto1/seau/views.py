from django.shortcuts import render

from .models import  Order

def index(request):
    aas = Order.objects.all
    return render(request, 'seau/index.html', {'aas': aas})


