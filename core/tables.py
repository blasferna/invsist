import django_tables2 as tables
from django.contrib.auth.models import User

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



class UserTable(EditableTable):
    class Meta:
        model = User
        fields = ("username", "first_name", "Last_name", "is_active",)
