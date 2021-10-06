from django.contrib import admin
from django.urls import path

from prima_wisata import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('wisata/', views.wisata, name='wisata'),
    path('chat/', views.chat, name='chat'),
]
