from django.contrib import admin

from apps.system_console.models import (
    AccessRules,
    BusinessElement,
)

admin.site.register([BusinessElement, AccessRules])