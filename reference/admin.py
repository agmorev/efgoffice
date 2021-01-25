from django.contrib import admin
from .models import CustomsRegime, VehicleType, Carrier, Consignee, Consignor, Forwarder, Document, Currency, CustomsOffice
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import ugettext_lazy as _


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_code', 'document_name')
    list_filter = ['document_type']
    ordering = ['document_code']
    search_fields = ('document_code', 'document_name')
    fieldsets = (
        (_('КЛАСИФІКАТОР документів'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['document_type', 'document_code', 'document_name'],
        }),
    )


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_code', 'currency_letter', 'currency_name')
    ordering = ['currency_code']
    search_fields = ('currency_code', 'currency_letter', 'currency_name')
    fieldsets = (
        (_('КЛАСИФІКАТОР іноземних валют'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['currency_code', 'currency_letter', 'currency_name'],
        }),
    )


@admin.register(CustomsOffice)
class CustomsOfficeAdmin(ImportExportModelAdmin):
    list_display = ('office_code', 'office_name')
    ordering = ['office_code']
    search_fields = ('office_code', 'office_name')
    fieldsets = (
        (_('КЛАСИФІКАТОР митних підрозділів'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['office_code', 'office_name'],
        }),
    )


@admin.register(CustomsRegime)
class CustomsRegimeAdmin(admin.ModelAdmin):
    list_display = ('regime_code', 'regime_name')
    ordering = ['regime_code']
    search_fields = ('regime_code', 'regime_name')
    list_filter = ('regime_type',)
    fieldsets = (
        (_('КЛАСИФІКАТОР митних режимів'), {
            'classes': ('wide', 'extrapretty'),
            'fields': [('regime_type', 'regime_type_code'), ('regime_code', 'regime_name')],
        }),
    )


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('vehicle_code', 'vehicle_name')
    ordering = ['vehicle_code']
    list_filter = ('vehicle_type',)
    search_fields = ['vehicle_code', 'vehicle_name']
    fieldsets = (
        (_('КЛАСИФІКАТОР видів транспорту'), {
            'classes': ('wide', 'extrapretty'),
            'fields': [('vehicle_type', 'vehicle_type_code'), ('vehicle_code', 'vehicle_name')],
        }),
    )


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('carrier_name', 'carrier_address', 'carrier_code', 'carrier_tax')
    ordering = ['carrier_name']
    search_fields = ('carrier_name', 'carrier_address', 'carrier_code', 'carrier_tax')
    list_filter = ('carrier_country',)
    fieldsets = (
        (_('ПЕРЕВІЗНИК'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['carrier_country', ('carrier_name', 'carrier_address'), ('carrier_code', 'carrier_tax')],
        }),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Consignor)
class ConsignorAdmin(admin.ModelAdmin):
    list_display = ('consignor_name', 'consignor_address', 'consignor_code', 'consignor_tax')
    ordering = ['consignor_name']
    search_fields = ('consignor_name', 'consignor_address', 'consignor_code', 'consignor_tax')
    list_filter = ('consignor_country',)
    fieldsets = (
        (_('ВІДПРАВНИК'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['consignor_country', ('consignor_name', 'consignor_address'), ('consignor_code', 'consignor_tax')],
        }),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Consignee)
class ConsigneeAdmin(admin.ModelAdmin):
    list_display = ('consignee_name', 'consignee_address', 'consignee_code', 'consignee_tax')
    ordering = ['consignee_name']
    search_fields = ('consignee_name', 'consignee_address', 'consignee_code', 'consignee_tax')
    list_filter = ('consignee_name',)
    fieldsets = (
        (_('ОДЕРЖУВАЧ'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['consignee_country', ('consignee_name', 'consignee_address'), ('consignee_code', 'consignee_tax')],
        }),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Forwarder)
class ForwarderAdmin(admin.ModelAdmin):
    list_display = ('forwarder_name', 'forwarder_address', 'forwarder_code', 'forwarder_tax')
    ordering = ['forwarder_name']
    search_fields = ('forwarder_name', 'forwarder_address', 'forwarder_code', 'forwarder_tax')
    list_filter = ('forwarder_country',)
    fieldsets = (
        (_('ЕКСПЕДИТОР'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['forwarder_country', ('forwarder_name', 'forwarder_address'), ('forwarder_code', 'forwarder_tax')],
        }),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()