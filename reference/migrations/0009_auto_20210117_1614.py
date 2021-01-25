# Generated by Django 3.1.2 on 2021-01-17 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reference', '0008_customsoffice'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_consignee', to='user.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consignor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_consignor', to='user.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forwarder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_forwarder', to='user.user'),
            preserve_default=False,
        ),
    ]