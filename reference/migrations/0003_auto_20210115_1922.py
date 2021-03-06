# Generated by Django 3.1.2 on 2021-01-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_auto_20210115_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='customsregime',
            name='regime_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='напрямок переміщення'),
        ),
        migrations.AddField(
            model_name='customsregime',
            name='regime_type_code',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='код напрямку'),
        ),
        migrations.AlterField(
            model_name='customsregime',
            name='regime_code',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='код режиму'),
        ),
    ]
