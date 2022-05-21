# Generated by Django 4.0.4 on 2022-05-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuloModel',
            fields=[
                ('modulo_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del modulo')),
            ],
            options={
                'verbose_name': 'modulo',
                'verbose_name_plural': 'modulos',
                'db_table': 'modulo',
            },
        ),
    ]