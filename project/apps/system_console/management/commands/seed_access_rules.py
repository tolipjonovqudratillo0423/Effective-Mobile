from django.core.management.base import BaseCommand
from apps.system_console.models import BusinessElement, AccessRules

class Command(BaseCommand):
    help = "Seeds business elements and access rules"

    def handle(self, *args, **kwargs):
        order, _ = BusinessElement.objects.get_or_create(title="order")
        product, _ = BusinessElement.objects.get_or_create(title="product")

        rules = [
            # admin — полный доступ
            {"role": "admin", "element": order, "can_read": True, "can_create": True, "can_update": True, "can_delete": True},
            {"role": "admin", "element": product, "can_read": True, "can_create": True, "can_update": True, "can_delete": True},
            
            # manager — без удаления
            {"role": "manager", "element": order, "can_read": True, "can_create": True, "can_update": True, "can_delete": False},
            {"role": "manager", "element": product, "can_read": True, "can_create": True, "can_update": True, "can_delete": False},
            
            # user — только чтение
            {"role": "user", "element": order, "can_read": True, "can_create": False, "can_update": False, "can_delete": False},
            {"role": "user", "element": product, "can_read": True, "can_create": False, "can_update": False, "can_delete": False},
            
            # guest — ничего
            {"role": "guest", "element": order, "can_read": False, "can_create": False, "can_update": False, "can_delete": False},
            {"role": "guest", "element": product, "can_read": False, "can_create": False, "can_update": False, "can_delete": False},
        ]

        for rule in rules:
            AccessRules.objects.get_or_create(**rule)

        self.stdout.write(self.style.SUCCESS("Seeded access rules!"))