# Generated by Django 2.1.4 on 2019-02-06 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_auto_20190206_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='scheduled_on',
            new_name='date',
        ),
    ]
