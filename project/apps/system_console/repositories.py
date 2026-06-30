from apps.system_console.models import (
    BusinessElement,
    AccessRules
)

#======================================================================
# Business Element Repository
#======================================================================
 
class BusinessElementRepository:
    def __init__(self):
        self.model = BusinessElement
    
    @staticmethod  
    def get_all():
        return BusinessElement.objects.filter(is_active=True)
  
  
    
#======================================================================
# Access Rules Repository
#======================================================================
    
class AccessRulesRepository:
    def __init__(self):
        self.model = AccessRules
    
    @staticmethod  
    def get_all():
        return (AccessRules.objects
                .select_related(
                    "element"
                )
                .filter(is_active=True)
                )