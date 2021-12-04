from django.urls import reverse_lazy
from menu import Menu, MenuItem

Menu.add_item("main", MenuItem("Usuarios",
                               reverse_lazy("user_list")))
