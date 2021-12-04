from core.mixins import SearchViewMixin
from core.views import CreateWithFormsetInlinesView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableMixin
from inventory.tables import BuyerTable, SupplierTable
from store.forms import OrderForm

from store.inlines import OrderDetailInline
from store.models import Buyer, Order, Supplier

from .tables import OrderTable


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

class OrderListView(SearchViewMixin, SingleTableMixin, ListView):
    model = Order
    table_class = OrderTable
    search_fields = ['supplier__name', 'buyer__name']
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'buyer_update'
        return context


class OrderCreateView(CreateWithFormsetInlinesView):
    model = Order
    form_class = OrderForm
    template_name = 'store/order_create.html'
    inlines = [OrderDetailInline]

    def get_success_url(self):
        return reverse_lazy('order_list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
