from extra_views.advanced import InlineFormSetFactory
from .models import OrderDetail
from .forms import OrderDetForm

class OrderDetailInline(InlineFormSetFactory):
    model = OrderDetail
    form_class = OrderDetForm
    factory_kwargs = {'extra':1 }
    fields =  ['product', 'quantity', 'price']
