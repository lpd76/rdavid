# Generated by Django 2.1.4 on 2019-02-05 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20190205_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(limit_choices_to={'psychologue': True}, on_delete=django.db.models.deletion.CASCADE, to='client.Client'),
        ),
    ]
