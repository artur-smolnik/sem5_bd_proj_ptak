# Generated by Django 3.1.2 on 2020-11-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaW', '0004_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('color', models.CharField(max_length=20, null=True)),
                ('price', models.FloatField(max_length=20, null=True)),
                ('amount', models.IntegerField(max_length=5, null=True)),
            ],
        ),
    ]
