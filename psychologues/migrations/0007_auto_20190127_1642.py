# Generated by Django 2.1.4 on 2019-01-27 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychologues', '0006_remove_competence_clientele'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orientation',
            options={'ordering': ['nom_fr'], 'verbose_name_plural': 'Orientations'},
        ),
        migrations.RenameField(
            model_name='orientation',
            old_name='nom',
            new_name='nom_fr',
        ),
        migrations.RenameField(
            model_name='orientation',
            old_name='name',
            new_name='non_en',
        ),
    ]
