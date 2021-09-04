from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from store.models import Buyer
from inventory.mixins import SearchViewMixin

class BuyerListView(SearchViewMixin, ListView):
    model = Buyer
    search_fields = ['name']
    template_name = 'store/buyer_list.html'

class BuyerCreateView(CreateView):
    model = Buyer
    template_name = 'store/buyer_create.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('buyer_list')

class BuyerUpdateView(UpdateView):
    model = Buyer
    template_name = 'store/buyer_update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('buyer_list')

class BuyerDeleteView(DeleteView):
    model = Buyer
    template_name = 'store/buyer_delete.html'
    # success_url = reverse_lazy('buyer_list')
    def get_success_url(self):
        return reverse_lazy('buyer_list')