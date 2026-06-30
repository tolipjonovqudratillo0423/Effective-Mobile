from rest_framework.permissions import BasePermission

from apps.authentication.permissions import (
    HasPermission
)
from apps.authentication.models import User

class IsAdmin(BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return request.user.role == User.RolesChoices.ADMIN
    
    
