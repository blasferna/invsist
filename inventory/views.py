from core.mixins import SearchViewMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableMixin

from inventory.models import Brand, Category, Product
from inventory.tables import BrandTable, CategoryTable, ProductTable

@login_required
def main(request):
    return render(request, template_name='home.html', context={})

class BrandListView(LoginRequiredMixin, SearchViewMixin, SingleTableMixin, ListView):
    model = Brand
    table_class = BrandTable
    paginate_by = 6
    search_fields = ['name']
    template_name = 'inventory/brand_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'brand_update'
        return context

class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    template_name = 'inventory/brand_create.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("brand_list")

class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = Brand
    template_name = 'inventory/brand_update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("brand_list")

class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'inventory/brand_delete.html'

    def get_success_url(self):
        return reverse_lazy("brand_list")

class CategoryListView(LoginRequiredMixin, SearchViewMixin, SingleTableMixin, ListView):
    model = Category
    table_class = CategoryTable
    search_fields = ['name']
    template_name = 'inventory/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'category_update'
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'inventory/category_create.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("category_list")

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'inventory/category_update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("category_list")

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'inventory/category_delete.html'

    def get_success_url(self):
        return reverse_lazy("category_list")

class ProductListView(LoginRequiredMixin, SearchViewMixin, SingleTableMixin, ListView):
    model = Product
    table_class = ProductTable
    search_fields = ['name', 'barcode', 'brand__name']
    template_name = 'inventory/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'product_update'
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'inventory/product_create.html'
    fields = ['name', 'barcode', 'brand', 'category', 'cost', 'price']

    def get_success_url(self):
        return reverse_lazy("product_list")

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'inventory/product_update.html'
    fields = ['name', 'barcode', 'brand', 'category', 'cost', 'price']

    def get_success_url(self):
        return reverse_lazy("product_list")

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/product_delete.html'

    def get_success_url(self):
        return reverse_lazy("product_list")
