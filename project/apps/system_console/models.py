from django.db import models

from apps.common.models import (
    BaseModel
)
from apps.authentication.models import User
# Create your models here.



#======================================================================
# Business Element
#======================================================================

class BusinessElement(BaseModel):
    
    title = models.CharField(
        max_length=100
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Business Element"
        verbose_name_plural = "Business Elements"
    


#======================================================================
# Access Rules
#======================================================================

class AccessRules(BaseModel):
    
    role = models.CharField(
        choices=User.RolesChoices.choices,
        max_length=20
    )
    element = models.ForeignKey(
        BusinessElement,
        related_name="accessrules", 
        on_delete=models.CASCADE
    )
    can_read = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.role 
    
    