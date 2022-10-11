from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import AutoForm, ClientForm, WorkForm, ProductForm,OrderForm
from .models import  Order, Auto, Client, Work, Product

def index(request):
    aas = Order.objects.order_by('-datepub')

    return render(request, 'seau/index.html', {'aas': aas})

 


class AutoCreateView(CreateView):
    template_name = 'seau/create.html'
    form_class = AutoForm
    success_url = '/seau/add4/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClientCreateView(CreateView):
    template_name = 'seau/createClient.html'
    form_class = ClientForm
    success_url = '/seau/add4/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WorkCreateView(CreateView):
    template_name = 'seau/createWork.html'
    form_class = WorkForm
    success_url = '/seau/add4/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductCreateView(CreateView):
    template_name = 'seau/createProduct.html'
    form_class = ProductForm
    success_url = '/seau/add4/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class OrderCreateView(CreateView):
    template_name = 'seau/createOrder.html'
    form_class = OrderForm
    success_url = '/seau/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
