from rest_framework.permissions import BasePermission

from apps.authentication.serivces import (
    AccessService
)

class HasPermission(BasePermission):
    action = ""
    element = ""
    
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False
        
        access = AccessService.has_permission(
            role=request.user.role,
            action=self.action,
            element_title=self.element
        )
        
        if not access:
            return False
        
        return True
    
    
        