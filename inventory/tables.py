import django_tables2 as tables
from inventory.models import Brand, Category, Product
from store.models import Buyer, Supplier

class BaseTable(tables.Table):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = "django_tables2/bootstrap4.html"


class SingleTable(BaseTable):
    def __init__(self, *args, **kwargs):
        kwargs['empty_text']  =  "Sin resultados." 
        super().__init__(*args, **kwargs) 

class EditableTable(BaseTable):
    def __init__(self, *args, **kwargs):
        kwargs['empty_text']  =  "Sin resultados."
        kwargs['extra_columns'] = [('editar', tables.TemplateColumn(template_name="includes/edit_button.html", verbose_name="Editar", orderable=False))]
        super().__init__(*args, **kwargs)


## definiciones

class BrandTable(EditableTable):
    class Meta:
        model = Brand
        fields = ("name",)

class CategoryTable(EditableTable):
    class Meta:
        model = Category
        fields = ("name",)

class ProductTable(EditableTable):
    class Meta:
        model = Product
        fields = ("name", "barcode", "brand", "category",)

class BuyerTable(EditableTable):
    class Meta:
        model = Buyer
        fields = ("name", "addres",)

class SupplierTable(EditableTable):
    class Meta:
        model = Supplier
        fields = ("name", "addres",)