from django.db import models



#======================================================================
# Base Model
#======================================================================

class BaseModel(models.Model):
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
