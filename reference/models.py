from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from user.models import User


class Currency(models.Model):
    currency_code = models.CharField(
        _('код'),
        max_length=3,
        null=True,
        blank=True)
    currency_letter = models.CharField(
        _('літерний код'),
        max_length=3,
        null=True,
        blank=True)
    currency_name = models.CharField(
        _('назва'),
        max_length=255,
        null=True,
        blank=True)
    
    class Meta:
        verbose_name = _('валюта')
        verbose_name_plural = _('валюти')
    
    def __str__(self):
        return str(' '.join([self.currency_letter]))


class Document(models.Model):
    document_type = models.CharField(
        _('тип'),
        max_length=255,
        null=True,
        blank=True)
    document_code = models.CharField(
        _('код'),
        max_length=4,
        null=True,
        blank=True)
    document_name = models.CharField(
        _('найменування'),
        max_length=255,
        null=True,
        blank=True)
    
    class Meta:
        verbose_name = _('документ')
        verbose_name_plural = _('документи')
    
    def __str__(self):
        return str(' | '.join([self.document_code, self.document_name]))


class CustomsOffice(models.Model):
    office_code = models.CharField(
        _('код підрозділу'),
        max_length=8,
        null=True,
        blank=True)
    office_name = models.CharField(
        _('назва'),
        max_length=255,
        null=True,
        blank=True)
    
    class Meta:
        verbose_name = _('митний підрозділ')
        verbose_name_plural = _('митні підрозділи')
    
    def __str__(self):
        return str(' '.join([self.office_code, self.office_name]))


class CustomsRegime(models.Model):
    regime_type = models.CharField(
        _('напрямок переміщення'),
        max_length=255,
        null=True,
        blank=True)
    regime_type_code = models.CharField(
        _('код напрямку'),
        max_length=1,
        null=True,
        blank=True)
    regime_code = models.CharField(
        _('код режиму'),
        max_length=2,
        null=True,
        blank=True)
    regime_name = models.CharField(
        _('назва'),
        max_length=255,
        null=True,
        blank=True)
    
    class Meta:
        verbose_name = _('митний режим')
        verbose_name_plural = _('митні режими')
    
    def __str__(self):
        return str(' '.join([self.regime_code, self.regime_name]))


class VehicleType(models.Model):
    vehicle_type = models.CharField(
        _('тип транспорту'),
        max_length=255,
        null=True,
        blank=True)
    vehicle_type_code = models.CharField(
        _('код типу'),
        max_length=1,
        null=True,
        blank=True)
    vehicle_code = models.CharField(
        _('код транспорту'),
        max_length=2,
        null=True,
        blank=True)
    vehicle_name = models.CharField(
        _('назва'),
        max_length=255,
        null=True,
        blank=True)
    
    class Meta:
        verbose_name = _('вид транспорту')
        verbose_name_plural = _('види транспорту')
    
    def __str__(self):
        return str(' '.join([self.vehicle_code, self.vehicle_name]))


class Carrier(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='user_carrier')
    carrier_country = CountryField(
        _('країна реєстрації'),
        blank_label=_('Оберіть країну...'),
        blank=True)
    carrier_name = models.CharField(
        _('назва компанії'),
        max_length=255,
        null=True,
        blank=True)
    carrier_address = models.CharField(
        _('адреса'),
        max_length=255,
        null=True,
        blank=True)
    carrier_code = models.CharField(
        _('ЄДРПОУ/ДРФО'),
        max_length=8,
        null=True,
        blank=True)
    carrier_tax = models.CharField(
        _('ІПН'),
        max_length=12,
        null=True,
        blank=True)   
    
    class Meta:
        verbose_name = _('перевізник')
        verbose_name_plural = _('перевізники')
    
    def __str__(self):
        return str(self.carrier_name)


class Consignor(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='user_consignor')
    consignor_country = CountryField(
        _('країна реєстрації'),
        blank_label=_('Оберіть країну...'),
        blank=True)
    consignor_name = models.CharField(
        _('назва компанії'),
        max_length=255,
        null=True,
        blank=True)
    consignor_address = models.CharField(
        _('адреса'),
        max_length=255,
        null=True,
        blank=True)
    consignor_code = models.CharField(
        _('ЄДРПОУ/ДРФО'),
        max_length=8,
        null=True,
        blank=True)
    consignor_tax = models.CharField(
        _('ІПН'),
        max_length=12,
        null=True,
        blank=True)   
    
    class Meta:
        verbose_name = _('відправник')
        verbose_name_plural = _('відправники')
    
    def __str__(self):
        return str(self.consignor_name)


class Consignee(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='user_consignee')
    consignee_country = CountryField(
        _('країна реєстрації'),
        blank_label=_('Оберіть країну...'),
        blank=True)
    consignee_name = models.CharField(
        _('назва компанії'),
        max_length=255,
        null=True,
        blank=True)
    consignee_address = models.CharField(
        _('адреса'),
        max_length=255,
        null=True,
        blank=True)
    consignee_code = models.CharField(
        _('ЄДРПОУ/ДРФО'),
        max_length=8,
        null=True,
        blank=True)
    consignee_tax = models.CharField(
        _('ІПН'),
        max_length=12,
        null=True,
        blank=True)   
    
    class Meta:
        verbose_name = _('одержувач')
        verbose_name_plural = _('одержувачі')
    
    def __str__(self):
        return str(self.consignee_name)


class Forwarder(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='user_forwarder')
    forwarder_country = CountryField(
        _('країна реєстрації'),
        blank_label=_('Оберіть країну...'),
        blank=True)
    forwarder_name = models.CharField(
        _('назва компанії'),
        max_length=255,
        null=True,
        blank=True)
    forwarder_address = models.CharField(
        _('адреса'),
        max_length=255,
        null=True,
        blank=True)
    forwarder_code = models.CharField(
        _('ЄДРПОУ/ДРФО'),
        max_length=8,
        null=True,
        blank=True)
    forwarder_tax = models.CharField(
        _('ІПН'),
        max_length=12,
        null=True,
        blank=True)   
    
    class Meta:
        verbose_name = _('експедитор')
        verbose_name_plural = _('експедитори')
    
    def __str__(self):
        return str(self.forwarder_name)