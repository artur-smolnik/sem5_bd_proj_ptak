# Generated by Django 3.1.2 on 2020-12-17 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaW', '0005_equipment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='Workers',
        ),
    ]
