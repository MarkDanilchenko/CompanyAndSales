# Generated by Django 4.2.6 on 2023-10-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=100, verbose_name='Customer name')),
                ('surname', models.CharField(help_text='Enter surname', max_length=100, verbose_name='Customer surname')),
                ('email', models.EmailField(help_text='Enter email', max_length=254, unique=True, verbose_name='Customer email')),
                ('phone', models.CharField(help_text='Enter phone', max_length=12, unique=True, verbose_name='Customer phone')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=100, unique=True, verbose_name='Item name')),
                ('description', models.TextField(help_text='Enter description', verbose_name='Item description')),
            ],
        ),
    ]
