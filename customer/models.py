from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    MaxLengthValidator,
                                    MinLengthValidator)


class Company(models.Model):
    name = models.CharField(_('назва'),
        max_length=255,
        null=True,
        blank=True)
    code = models.CharField(_('ЄДРПОУ'),
        max_length=8,
        null=True,
        blank=True)
    tax = models.CharField(_('ІПН'),
        max_length=10,
        null=True,
        blank=True)   
    address = models.CharField(_('адреса'),
        max_length=255,
        null=True,
        blank=True) 
    country = CountryField(
        _('країна'),
        blank_label=_('Оберіть країну...'),
        blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    middle_name = models.CharField(
        _('по батькові'),
        max_length=50,
        null=True,
        blank=True)
    position = models.CharField(_('посада'),
        max_length=255,
        null=True,
        blank=True)
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='user')

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username