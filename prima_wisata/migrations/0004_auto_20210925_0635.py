# Generated by Django 3.2.7 on 2021-09-25 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prima_wisata', '0003_respon_pertanyaan_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('biaya', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='tempat',
            name='biaya_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prima_wisata.biaya'),
        ),
    ]