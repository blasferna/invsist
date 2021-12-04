from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms.formsets import all_valid
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django_tables2 import SingleTableMixin
from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from core.mixins import FormsetInlinesMetaMixin, SearchViewMixin
from core.tables import UserTable

from .forms import CustomUserChangeForm, CustomUserCreationForm


class CreateWithFormsetInlinesView(FormsetInlinesMetaMixin, CreateWithInlinesView):
    """
    Create view con soporte para formset inlines
    """
    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #initial_object = self.object
        inlines = self.construct_inlines()
        try:
            with transaction.atomic():
                if form.is_valid():
                    self.object = form.save(commit=False)
                    form_validated = True
                else:
                    form_validated = False
                # Loop through inlines to set master instance
                for inline in inlines:
                    inline.instance = form.instance

                if all_valid(inlines) and form_validated:
                    response = self.forms_valid(form, inlines)
                    self.run_form_extra_validation(form, inlines)
                    if not form.errors and response:
                        return response
                raise ValidationError('Error')
        except ValidationError:
            pass
        #self.object = initial_object
        return self.forms_invalid(form, inlines)


class UpdateWithFormsetInlinesView(FormsetInlinesMetaMixin, UpdateWithInlinesView):
    """
    Update view con soporte para formset inlines
    """

    def run_form_extra_validation(self, form, inlines):
        """ ejecutar validaciones adicionales de formularios """

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        initial_object = self.object
        inlines = self.construct_inlines()
        try:
            with transaction.atomic():
                if form.is_valid():
                    self.object = form.save(commit=False)
                    form_validated = True
                else:
                    form_validated = False
                # Loop through inlines to set master instance
                for inline in inlines:
                    inline.instance = form.instance

                if all_valid(inlines) and form_validated:
                    response = self.forms_valid(form, inlines)
                    self.run_form_extra_validation(form, inlines)
                    if not form.errors and response:
                        return response
                raise ValidationError('Error')
        except ValidationError:
            pass
        self.object = initial_object
        return self.forms_invalid(form, inlines)


class UserListView(LoginRequiredMixin, SearchViewMixin, SingleTableMixin, ListView):
    model = User
    table_class = UserTable
    search_fields = ['username', 'first_name']
    template_name = 'registration/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'user_update'
        return context

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/user_create.html'

    def get_success_url(self):
        return reverse_lazy('user_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'registration/user_update.html'

    def get_success_url(self):
        return reverse_lazy("user_list")

