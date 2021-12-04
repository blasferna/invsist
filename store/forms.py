import calculation
from core.layout import CancelButton, DeleteButton, Formset
from core.widgets import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Button, ButtonHolder, Column, Div, Fieldset,
                                 Layout, Row, Submit, Field)
from django import forms
from django.db.models import fields

from .models import Order, OrderDetail


class OrderForm(forms.ModelForm):
    total = forms.DecimalField(
        widget=calculation.SumInput('subtotal',   attrs={'readonly':True}),
    )
    total_iva = forms.DecimalField(
        widget=calculation.SumInput('iva',   attrs={'readonly':True}),
    )
    class Meta:
        model = Order
        fields = ['type', 'date', 'supplier', 'buyer', 'observation']
        widgets = { 'date':DateInput }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['total'].label = False
        self.fields['total_iva'].label = False
        self.helper.layout = Layout(
            Row(Column("type"), Column("date")),
            "supplier",
            "buyer",
            "observation",
            Fieldset(
                u'Artículos',
                Formset(
                    "OrderDetailInline"
                )
            ),
            Row(
                Column(HTML("<div class='w-100'></div>")), Column(HTML('<span class="w-100"> Total: </span>'), css_class="text-right"), Column("total")
            ), 
            Row(
                Column(HTML("<div class='w-100'></div>")), Column(HTML('<span class="w-100"> Total IVA: </span>'), css_class="text-right"), Column("total_iva")
            ),
            Row(
                Div(Submit("submit", "Guardar"), HTML("""<a class="btn btn-secondary" href="{% url 'order_list' %}"> Cancelar</a>""" ))
            )
           
        )

class OrderDetForm(forms.ModelForm):
    subtotal = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*price', attrs={'readonly':True})
    )
    iva = forms.DecimalField(
        widget=calculation.FormulaInput('parseFloat(subtotal/11).toFixed(0)', attrs={'readonly':True})
    )
    class Meta:
        model = OrderDetail
        fields = ['product', 'price', 'quantity', 'subtotal']

