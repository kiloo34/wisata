# Generated by Django 3.2.7 on 2021-09-25 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prima_wisata', '0004_auto_20210925_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pertanyaan',
            old_name='kategori_id',
            new_name='kategori',
        ),
        migrations.RenameField(
            model_name='pertanyaan',
            old_name='tempat_id',
            new_name='tempat',
        ),
        migrations.RenameField(
            model_name='respon',
            old_name='kategori_id',
            new_name='kategori',
        ),
        migrations.RenameField(
            model_name='respon',
            old_name='pertanyaan_id',
            new_name='pertanyaan',
        ),
        migrations.RenameField(
            model_name='respon',
            old_name='tempat_id',
            new_name='tempat',
        ),
        migrations.RenameField(
            model_name='tempat',
            old_name='biaya_id',
            new_name='biaya',
        ),
    ]
