from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
# from django.core.validators import (MaxValueValidator,
#                                     MinValueValidator,
#                                     MaxLengthValidator,
#                                     MinLengthValidator)
from user.models import User
from django.http import request
from reference.models import Carrier, Consignee, Consignor, Currency, CustomsOffice, CustomsRegime, Document, Forwarder, VehicleType


class Order(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='user')
    order_number = models.CharField(
        _('номер заявки'),
        max_length=5,
        null=True,
        blank=True)
    order_date = models.DateField(
        _('дата формування')
    )
    regime = models.ForeignKey(
        CustomsRegime,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='regime',
        verbose_name=_('митний режим')
    )
    vehicle = models.ForeignKey(
        VehicleType,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='vehicle',
        verbose_name=_('тип транспорту')
    )
    carrier = models.ForeignKey(
        Carrier,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='carrier',
        verbose_name=_('перевізник')
    )
    consignor = models.ForeignKey(
        Consignor,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='consignor',
        verbose_name=_('відправник')
    )
    consignee = models.ForeignKey(
        Consignee,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='consignee',
        verbose_name=_('одержувач')
    )
    forwarder = models.ForeignKey(
        Forwarder,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='forwarder',
        verbose_name=_('експедитор')
    )
    customs_departure = models.ForeignKey(
        CustomsOffice,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='departure',
        verbose_name=_('митниця відправлення')
    )
    customs_destination = models.ForeignKey(
        CustomsOffice,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='destination',
        verbose_name=_('митниця призначення')
    )
    driver_name = models.CharField(
        _('ПІБ водія'),
        max_length=255,
        null=True,
        blank=True)
    driver_phone = PhoneNumberField(
        _('контактний телефон'),
        null=True,
        blank=True)
    vehicle_number = models.CharField(
        _('номер ТЗ'),
        max_length=255,
        blank=True,
        null=True)

    class Meta:
        verbose_name = _('заявка')
        verbose_name_plural = _('заявки')
    
    def __str__(self):
        return str(self.id)


class OrderDocument(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='order_document')  
    document = models.ForeignKey(
        Document,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='document',
        verbose_name=_('вид'))
    document_number = models.CharField(
        _('номер'),
        max_length=25,
        null=True,
        blank=True)
    document_date = models.DateField(
        _('дата'))

    class Meta:
        verbose_name = _('документ до заявки')
        verbose_name_plural = _('документи до заявки')
    
    def __str__(self):
        return str(' '.join([self.document_number, self.document_date]))

class Goods(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='order_goods')
    cargo_name = models.CharField(
        _('найменування товару'),
        max_length=1000,
        null=True,
        blank=True)
    cargo_code = models.CharField(
        _('код УКТЗЕД'),
        max_length=10,
        null=True,
        blank=True,
        # help_text=_('Код товару зазначається на менше ніж на рівні 4-х знаків')
    )
    cargo_weight = models.FloatField(
        _('вага товару, кг'),
        max_length=255,
        null=True,
        blank=True)
    cargo_addnumber = models.FloatField(
        _('додаткові одиниці'),
        max_length=255,
        null=True,
        blank=True,
        # help_text=_('Кількість товару в додаткових одиницях виміру (л., шт.)')
    )
    cargo_value = models.FloatField(
        _('фактурна вартість'),
        max_length=255,
        null=True,
        blank=True,
        # help_text=_('Вартість зазначається в валюті контракту/інвойсу')
    )
    cargo_currency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='currency',
        verbose_name=_('валюта')
    )
    cargo_value_uah = models.FloatField(
        _('вартість, грн'),
        max_length=255,
        null=True,
        blank=True,
        # help_text=_('Вартість зазначається в валюті контракту/інвойсу')
    )
    cargo_duties = models.FloatField(
        _('митні платежі, грн'),
        max_length=255,
        null=True,
        blank=True,
        # help_text=_('Сума митних платежів в разі імпорту')
    )

    class Meta:
        verbose_name = _('товар')
        verbose_name_plural = _('товари')
    
    def __str__(self):
        return str(self.cargo_code)