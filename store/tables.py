from .models import Order

from inventory.tables import EditableTable

class OrderTable(EditableTable):
    class Meta:
        model = Order
        fields = ("type", "date", "observation", "total")