from django.contrib import admin
from .models import Order
from user.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
import datetime
from order.models import Goods, OrderDocument
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin, ExportActionMixin


class OrderResource(resources.ModelResource):

    order_number = fields.Field(attribute='order_number', column_name='Заявка №')
    order_date = fields.Field(attribute='order_date', column_name='Дата')
    regime__regime_code = fields.Field(attribute='regime__regime_code', column_name='Режим')
    vehicle__vehicle_code = fields.Field(attribute='vehicle__vehicle_code', column_name='Вид ТЗ')
    customs_departure__office_code = fields.Field(attribute='customs_departure__office_code', column_name='Митниця відправлення')
    customs_destination__office_code = fields.Field(attribute='customs_destination__office_code', column_name='Митниця призначення')
    carrier__carrier_code = fields.Field(attribute='carrier__carrier_code', column_name='ЄДРПОУ перевізника')
    carrier__carrier_name = fields.Field(attribute='carrier__carrier_name', column_name='Перевізник')
    consignor__consignor_code = fields.Field(attribute='consignor__consignor_code', column_name='ЄДРПОУ відправника')
    consignor__consignor_name = fields.Field(attribute='consignor__consignor_name', column_name='Відправник')
    consignee__consignee_code = fields.Field(attribute='consignee__consignee_code', column_name='ЄДРПОУ одержувача')
    consignee__consignee_name = fields.Field(attribute='consignee__consignee_name', column_name='Одержувач')
    forwarder__forwarder_code = fields.Field(attribute='forwarder__forwarder_code', column_name='ЄДРПОУ експедитора')
    forwarder__forwarder_name = fields.Field(attribute='forwarder__forwarder_name', column_name='Експедитор')
    vehicle_number = fields.Field(attribute='vehicle_number', column_name='ТЗ №')
    
    class Meta:
        model = Order
        fields = (
        'order_number', 
        'order_date', 
        'regime__regime_code', 
        'vehicle__vehicle_code', 
        'customs_departure__office_code',
        'customs_destination__office_code',
        'carrier__carrier_code',
        'carrier__carrier_name', 
        'consignor__consignor_code',
        'consignor__consignor_name', 
        'consignee__consignee_code',
        'consignee__consignee_name', 
        'forwarder__forwarder_code', 
        'forwarder__forwarder_name', 
        'vehicle_number')


class DocumentsInline(admin.TabularInline):
    model = OrderDocument
    extra = 1
    fk_name = 'order'
    autocomplete_fields = ['document']


class GoodsInline(admin.StackedInline):
    model = Goods
    extra = 1
    fieldsets = (
        (_(''), {
            'classes': ('wide', 'extrapretty'),
            'fields': [
                ('cargo_name', 'cargo_code'), 
                ('cargo_weight', 'cargo_addnumber'), 
                ('cargo_value', 'cargo_currency'),
                ('cargo_value_uah', 'cargo_duties')
                ]
            }
        ),       
    )

    class Media:
        js = ('js/paycalc_btn.js',)

@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = OrderResource

    list_display = ('order_number', 'order_date', 'regime', 'vehicle')
    list_display_links = ('order_number', 'order_date', 'regime', 'vehicle')
    list_filter = (
        ('regime', admin.RelatedOnlyFieldListFilter),
        ('vehicle', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ('order_number', 'order_date', 'regime', 'vehicle')
    date_hierarchy = 'order_date'
    empty_value_display = _('-пусто-')
    autocomplete_fields = (
        'carrier', 
        'consignor', 
        'consignee', 
        'forwarder', 
        'regime', 
        'vehicle',
        'customs_departure',
        'customs_destination',
    )
    inlines = [
        DocumentsInline,
        GoodsInline,
    ]
    save_as = True
    save_as_continue = False
    # inlines = [UserCompanyInline]
    fieldsets = (
        (_('ЗАЯВКА про видачу фінансової гарантії'), {
            'classes': ('wide', 'extrapretty'),
            'fields': [('order_number','order_date')],
        }),
        (_('УЧАСНИКИ ЗОВНІШНЬОЕКОНОМІЧНОЇ ДІЯЛЬНОСТІ'), {
            'classes': ('wide', 'extrapretty'),
            'fields': [('carrier', 'forwarder'), ('consignor', 'consignee')]
        }),
        
        (_('ІНФОРМАЦІЯ ПРО ПЕРЕМІЩЕННЯ'), {
            'classes': ('wide', 'extrapretty'),
            'fields': [
                ('regime', 'vehicle'), 
                ('customs_departure', 'customs_destination'),
                'driver_name',
                'driver_phone',
                'vehicle_number'
            ]
        }),
        
    )

    # def get_form(self, request, obj=None, *args, **kwargs):
    #      form = super(OrderAdmin, self).get_form(request, obj, *args, **kwargs)
    #      form.base_fields['user'].initial = request.user
    #      return form
    
    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    # def clean(self):
    #     product_offer_price = self.cleaned_data.get('product_offer_price')
    #     product_mrp = self.cleaned_data.get('product_mrp')
    #     if product_offer_price > product_mrp:
    #         raise forms.ValidationError("Product offer price cannot be greater than Product MRP.")
    #     return self.cleaned_data
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.vehicle_number = obj.vehicle_number.replace(" ", ",")
        obj.save()