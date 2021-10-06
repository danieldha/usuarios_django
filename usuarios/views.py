from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, ListView

from usuarios.forms import CrearUsuarioForm, EditarUsuarioForm
from usuarios.models import Usuario


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_staff


class IndexView(TemplateView):
    template_name = 'index.html'


class CrearUsuarioView(StaffRequiredMixin, CreateView):
    model = Usuario
    form_class = CrearUsuarioForm
    success_url = reverse_lazy('usuarios:listar_usuario')


class ActualizarUsuarioView(StaffRequiredMixin, UpdateView):
    model = Usuario
    form_class = EditarUsuarioForm
    success_url = reverse_lazy('usuarios:listar_usuario')


class ListarUsuarioView(StaffRequiredMixin, ListView):
    model = Usuario
