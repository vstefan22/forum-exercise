from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import login

class LoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('forum_app:index')


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('forum_app:index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


