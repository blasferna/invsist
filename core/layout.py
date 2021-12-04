
from django.template.loader import render_to_string
from crispy_forms.utils import TEMPLATE_PACK, flatatt
from crispy_forms.layout import LayoutObject, TemplateNameMixin, Field


class BaseButton(TemplateNameMixin):
    def __init__(self, **kwargs):
        if not getattr(self, 'field_classes'):
            self.field_classes = ""
        self.id = kwargs.pop("css_id", "")
        self.attrs = {}

        if "css_class" in kwargs:
            self.field_classes += " %s" % kwargs.pop("css_class")

        self.flat_attrs = flatatt(kwargs)

class DeleteButton(BaseButton):
    def __init__(self, **kwargs):
        self.field_classes = "btn btn-danger"
        super().__init__(**kwargs)


    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        context.update({"delete_button": self})
        return render_to_string('includes/delete_button.html', context.flatten())


class PlanField(Field):
    template = template = "%s/planfield.html"
    def __init__(self, *args, **kwargs):
        self.field_classes = kwargs.get('css_class', "")
        super().__init__(*args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, extra_context=None, **kwargs):
        extra_context = {'field_class': self.field_classes}
        return super().render(form, form_style, context, template_pack=template_pack, extra_context=extra_context, **kwargs)

class CancelButton(BaseButton):
    def __init__(self, **kwargs):
        self.field_classes = "btn btn-secondary"

        super().__init__(**kwargs)
    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        context.update({"cancel_button": self})
        return render_to_string('includes/cancel_button.html', context.flatten())

class Formset(LayoutObject):
    template = "bootstrap4/table_inline_formset.html"
    stacked_template = "bootstrap4/stacked_inline_formset.html"
    
    def __init__(self,formset_name,  formset_title=None, template=None, css_class=None, stacked=False, stacked_class="sm:w-1/2 md:w-1/4"):
        self.formset_name = formset_name
        self.css_class = css_class
        self.formset_title = formset_title
        self.stacked_class = stacked_class

        # crispy_forms/layout.py:302 requires us to have a fields property
        self.fields = []

        # Overrides class variable with an instance level variable
        if template:
            self.template = template
        else:
            if stacked:
                self.template = self.stacked_template

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        formset = None
        inline_index = None

        if self.formset_name:
            try:
                formset = context[self.formset_name]
            except KeyError:
                try:
                    inline_index = context['formset_inlines_meta'][self.formset_name]['index']
                except KeyError:
                    pass

        if inline_index is not None:
            try:
                formset = context['inlines'][inline_index]
            except IndexError:
                pass

        if formset:
            context.update({
                'formset': formset,
                'css_class':self.css_class,
                'formset_title':self.formset_title,
                'stacked_class':self.stacked_class
            })
        else:
            return ''

        return render_to_string(self.template, context.flatten())
