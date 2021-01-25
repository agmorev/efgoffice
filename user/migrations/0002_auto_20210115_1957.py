# Generated by Django 3.1.2 on 2021-01-15 17:57

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='країна реєстрації'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='ЄДРПОУ/ДРФО'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company_tax',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='ІПН'),
        ),
    ]