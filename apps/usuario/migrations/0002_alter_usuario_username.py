# Generated by Django 4.0.4 on 2022-05-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del usuario'),
        ),
    ]
