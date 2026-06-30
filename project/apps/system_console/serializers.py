from rest_framework import serializers

from apps.system_console.models import (
    BusinessElement,
    AccessRules
)

#======================================================================
# BusinessElement Serializer
#======================================================================

class BusinessElementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessElement
        fields = [
            "title"
        ]
    
 
 
#======================================================================
# AccessRules Serializer
#======================================================================

class AccessRulesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AccessRules
        fields = [
            "role",
            "element",
            "can_read",
            "can_create",
            "can_update",
            "can_delete",
        ]
       
    