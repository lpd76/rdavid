# Generated by Django 2.1.4 on 2019-02-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientele', '0001_initial'),
        ('client', '0009_client_raison_consultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='famille_de_probleme',
            field=models.ManyToManyField(to='clientele.CategorieProbleme'),
        ),
    ]