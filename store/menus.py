from django.urls import reverse_lazy
from menu import Menu, MenuItem

Menu.add_item("main", MenuItem("Comprador",
                               reverse_lazy("buyer_list")))

Menu.add_item("main", MenuItem("Proveedor",
                               reverse_lazy("supplier_list")))


Menu.add_item("main", MenuItem("Movimientos",
                               reverse_lazy("order_list")))