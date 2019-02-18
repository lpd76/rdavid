# Generated by Django 2.1.4 on 2019-02-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20190204_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fr', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nom_fr'],
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='service',
        ),
        migrations.AddField(
            model_name='client',
            name='adress',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='code_postale',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='client',
            name='nom',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='prenom',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='rue',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='ville',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
