from django.urls import reverse_lazy
from menu import Menu, MenuItem

# Agregamos los menus al principal
Menu.add_item("main", MenuItem("Inicio",
                               reverse_lazy("main")))

Menu.add_item("main", MenuItem("Marcas",
                               reverse_lazy("brand_list")))

Menu.add_item("main", MenuItem("Categorias",
                               reverse_lazy("category_list")))

Menu.add_item("main", MenuItem("Productos",
                               reverse_lazy("product_list")))
