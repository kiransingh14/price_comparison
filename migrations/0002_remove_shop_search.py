# Generated by Django 3.1 on 2020-10-11 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_comparison', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='search',
        ),
    ]
