from django.contrib import admin

from apps.sales.models import (
    Product,
    Order,)

admin.site.register([Product, Order])