# Generated by Django 2.1.4 on 2019-02-04 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_client_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['phone']},
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]