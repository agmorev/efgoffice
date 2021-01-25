# Generated by Django 3.1.2 on 2021-01-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='vehicle_number',
        ),
        migrations.AddField(
            model_name='order',
            name='vehicle_number',
            field=models.ManyToManyField(related_name='_order_vehicle_number_+', to='order.Order'),
        ),
    ]