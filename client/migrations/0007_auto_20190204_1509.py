# Generated by Django 2.1.4 on 2019-02-04 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20190204_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_de_naissance',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(max_length=50),
        ),
    ]