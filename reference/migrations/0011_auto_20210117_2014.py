# Generated by Django 3.1.2 on 2021-01-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0010_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_code',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='код'),
        ),
    ]