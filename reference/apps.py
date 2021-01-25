from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReferenceConfig(AppConfig):
    name = 'reference'
    verbose_name = _('Довідники')
