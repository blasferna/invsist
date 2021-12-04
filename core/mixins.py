from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist

class SearchViewMixin:
    search_fields = None

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_fields:
            or_condition = Q()
            value = self.get_search_query()
            if value:
                for field in self.search_fields:
                    or_condition.add(Q(**{f"{field}__icontains": value}), Q.OR)
                queryset = queryset.filter(or_condition)

        return queryset

    def get_search_query(self):
        return self.request.GET.get('q', None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.get_search_query()
        context['search_placeholder'] = self.get_search_placeholder()
        return context
    

    def _get_model_name_by_lookup(self, lookup):
        model = self.model
        for name in lookup.split('__'):
            try:
                field = model._meta.get_field(name)
            except FieldDoesNotExist:
                # name is probably a lookup or transform such as __contains
                break
            if hasattr(field, 'related_model'):
                # field is a relation
                if field.related_model:
                    model = field.related_model
                
            else:
                # field is not a relation, any name that follows is
                # probably a lookup or transform
                break
        return model

    def get_search_placeholder(self):
        placeholder = ""
        labels=[]
        model = self.model
        for field in self.search_fields:
            if len(field.split('__')) == 1: 
                labels.append(model._meta.get_field(field).verbose_name)
            else:
                related = self._get_model_name_by_lookup(field)
                model_name = related._meta.verbose_name
                try:
                    field_name = field.split('__')[-1:][0]
                    label = related._meta.get_field(field_name).verbose_name
                    labels.append(f"{model_name}: {label}")
                except FieldDoesNotExist:
                    pass
        if labels:
            placeholder = ", ".join(map(str.capitalize, map(str, labels)))
        return placeholder


class FormsetInlinesMetaMixin(object):
    _formset_inlines_meta = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build_formset_inlines_meta()

    def build_formset_inlines_meta(self):
        if not hasattr(self, 'inlines'):
            return None

        for i, formset_class in enumerate(self.inlines):
            self._formset_inlines_meta[formset_class.__name__] = { 'index': i }

    def get_formset_inlines_meta(self):
        return self._formset_inlines_meta

    def get_context_data(self, **kwargs):
        """
            get and update context data
        """
        context = super().get_context_data(**kwargs)
        context['formset_inlines_meta'] = self.get_formset_inlines_meta()
        return context
