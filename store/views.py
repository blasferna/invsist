from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from store.models import Buyer, Supplier
from inventory.mixins import SearchViewMixin
from django_tables2 import SingleTableMixin
from inventory.tables import BuyerTable, SupplierTable

class BuyerListView(SearchViewMixin, SingleTableMixin, ListView):
    model = Buyer
    table_class = BuyerTable
    search_fields = ['name']
    template_name = 'store/buyer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'buyer_update'
        return context

class BuyerCreateView(CreateView):
    model = Buyer
    template_name = 'store/buyer_create.html'
    fields = ['name', 'addres']

    def get_success_url(self):
        return reverse_lazy('buyer_list')

class BuyerUpdateView(UpdateView):
    model = Buyer
    template_name = 'store/buyer_update.html'
    fields = ['name', 'addres']

    def get_success_url(self):
        return reverse_lazy('buyer_list')

class BuyerDeleteView(DeleteView):
    model = Buyer
    template_name = 'store/buyer_delete.html'
    # success_url = reverse_lazy('buyer_list')
    def get_success_url(self):
        return reverse_lazy('buyer_list')

class SupplierListView(SearchViewMixin, SingleTableMixin, ListView):
    model = Supplier
    table_class = SupplierTable
    search_fields = ['name']
    template_name = 'store/supplier_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'supplier_update'
        return context

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'store/supplier_create.html'
    fields = ['name', 'addres']

    def get_success_url(self):
        return reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'store/supplier_update.html'
    fields = ['name', 'addres']

    def get_success_url(self):
        return reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'store/supplier_delete.html'
    def get_success_url(self):
        return reverse_lazy('supplier_list')