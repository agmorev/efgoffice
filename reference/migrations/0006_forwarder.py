# Generated by Django 3.1.2 on 2021-01-15 19:45

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0005_carrier_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forwarder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forwarder_country', django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='країна реєстрації')),
                ('forwarder_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='назва компанії')),
                ('forwarder_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='адреса')),
                ('forwarder_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='ЄДРПОУ/ДРФО')),
                ('forwarder_tax', models.CharField(blank=True, max_length=12, null=True, verbose_name='ІПН')),
            ],
            options={
                'verbose_name': 'експедитор',
                'verbose_name_plural': 'експедитори',
            },
        ),
    ]