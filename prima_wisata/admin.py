from django.contrib import admin
from django.db import reset_queries
from prima_wisata.models import Tempat, Kategori, Pertanyaan, Respon
# Register your models here.

admin.site.register(Tempat)
admin.site.register(Kategori)
admin.site.register(Pertanyaan)
admin.site.register(Respon)
