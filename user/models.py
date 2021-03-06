from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    middle_name = models.CharField(
        _('по батькові'),
        max_length=50,
        null=True,
        blank=True)
    position = models.CharField(
        _('посада'),
        max_length=255,
        null=True,
        blank=True)
    phone = PhoneNumberField(
        _('контактний телефон'),
        null=True,
        blank=True)
    company_country = CountryField(
        _('країна реєстрації'),
        blank_label=_('Оберіть країну...'),
        blank=True)
    company_name = models.CharField(
        _('назва компанії'),
        max_length=255,
        null=True,
        blank=True)
    company_code = models.CharField(
        _('ЄДРПОУ/ДРФО'),
        max_length=8,
        null=True,
        blank=True)
    company_tax = models.CharField(
        _('ІПН'),
        max_length=12,
        null=True,
        blank=True)   
    company_address = models.CharField(
        _('адреса'),
        max_length=255,
        null=True,
        blank=True)

    class Meta:
        verbose_name = _('користувач')
        verbose_name_plural = _('користувачі')

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username