# Generated by Django 3.1.2 on 2020-11-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaW', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
