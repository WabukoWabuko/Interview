from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm

# Create your views here.

# Listing all products
class ProductListView(ListView):
    model = Product
    template_name = 'App/product_list.html'
    context_object_name = 'products'

# View a single product
class ProductDetailView(DetailView):
    model = Product
    template_name = 'App/product_detail.html'
    context_object_name = 'product'

# Create a new product
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'App/product_form.html'
    success_url = reverse_lazy('product_list')

# Update an existing product
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'App/product_form.html'
    success_url = reverse_lazy('product_list')

# Delete a product
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'App/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')