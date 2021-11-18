from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from prima_wisata.models import Tempat, Kategori, Pertanyaan, Respon
from django.core.paginator import Paginator

from django.contrib import messages

from .forms import *

# Create your views here.


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Akun ' + user + ' Berhasil dibuat, silakan login untuk melanjutkan', extra_tags='success')
            return redirect('login')

    konteks = {
        'title': 'register',
        'subtitle': '',
        'active': 'register',
        'form': form,
    }
    return render(request, 'registration/register.html', konteks)


def login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # if user.
            return redirect('dashboard')
        else:
            messages.info(request, 'Username atau password salah',
                          extra_tags='danger')

    konteks = {
        'title': 'login',
        'subtitle': '',
        'active': 'login',
        'form': form,
    }
    return render(request, 'registration/login.html', konteks)

def guest(request):

    

    return redirect(request, 'user/dashboard.html');

def logout(request):
    auth_logout(request)
    return redirect('index')


def index(request):
    konteks = {
        'title': 'landing',
        'subtitle': '',
        'active': 'landing',
    }
    return render(request, 'user/index.html', konteks)


@login_required
def dashboard(request):
    tempat = Tempat.objects.all()

    p = Paginator(tempat, 3)
    page = request.GET.get('page')
    objek = p.get_page(page)

    konteks = {
        'title': 'dashboard',
        'subtitle': '',
        'active': 'index',
        'wisata': objek,
    }
    return render(request, 'user/dashboard.html', konteks)


@login_required
def wisata(request):
    tempat = Tempat.objects.all()
    konteks = {
        'title': 'wisata',
        'subtitle': '',
        'active': 'wisata',
        'wisata': tempat,
    }
    return render(request, 'user/wisata.html', konteks)


@login_required
def chat(request):
    # tempat = Tempat.objects.all()
    konteks = {
        'title': 'chat',
        'subtitle': '',
        'active': 'chat',
        # 'wisata': tempat,
    }
    return render(request, 'user/chat.html', konteks)
