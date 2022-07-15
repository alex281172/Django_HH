from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegForm
from django.views.generic import CreateView, DetailView
from .models import ParsUser
from django.urls import reverse, reverse_lazy
from rest_framework.authtoken.models import Token
from django.http import JsonResponse


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'

class UserCreateView(CreateView):
    model = ParsUser
    template_name = 'usersapp/register.html'
    form_class = RegForm
    success_url = reverse_lazy('users:login')

class UserDetailView(DetailView):
    template_name = 'usersapp/profile.html'
    model = ParsUser

def update_token(request):
    user = request.user
    try:
        user.auth_token.delete()
        Token.objects.create(user=user)
    except:
        print('Нет')
        # создать
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))

def update_token_ajax(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else:
        # создать
        token = Token.objects.create(user=user)
    return JsonResponse({'key': token.key})


