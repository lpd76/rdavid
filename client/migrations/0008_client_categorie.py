# Generated by Django 2.1.4 on 2019-02-04 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20190204_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.Categorie'),
        ),
    ]
