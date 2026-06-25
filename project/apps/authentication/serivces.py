
from apps.authentication.models import (
    AccessRules
)


#======================================================================
# Access Service
#======================================================================

class AccessService:
    
    @staticmethod
    def has_permission(
        role,
        element_title,
        action,
    )-> bool:
        
        rule = (
            AccessRules.objects
            .filter(
                role=role,
                element__title=element_title
            ).first()
        )
        if not rule:
            return False
        
        return getattr(rule, f"can_{action}", False)
