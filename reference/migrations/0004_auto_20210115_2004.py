# Generated by Django 3.1.2 on 2021-01-15 18:04

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_auto_20210115_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='carrier_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='країна реєстрації'),
        ),
        migrations.AddField(
            model_name='consignee',
            name='consignee_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='країна реєстрації'),
        ),
        migrations.AddField(
            model_name='consignor',
            name='consignor_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='країна реєстрації'),
        ),
    ]
