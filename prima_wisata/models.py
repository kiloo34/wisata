from django.db import models

# Create your models here.


class Biaya(models.Model):
    nama = models.CharField(max_length=50)
    biaya = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.nama


class Tempat(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.TextField()
    desa = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    buka = models.CharField(max_length=10)
    tutup = models.CharField(max_length=10)
    biaya = models.ForeignKey(Biaya, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nama


class Kategori(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nama


class Pertanyaan(models.Model):
    text = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tempat = models.ForeignKey(Tempat, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.text


class Respon(models.Model):
    text = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    pertanyaan = models.ForeignKey(
        Pertanyaan, on_delete=models.CASCADE, null=True)
    tempat = models.ForeignKey(Tempat, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.text
