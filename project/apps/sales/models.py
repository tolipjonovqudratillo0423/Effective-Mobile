from django.db import models

from apps.common.models import (
    BaseModel
)



#======================================================================
# Product 
#======================================================================

class Product(BaseModel):
    
    name = models.CharField(
        max_length=100
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    def __str__(self):
        return self.name
    

#======================================================================
# Order 
#======================================================================

class Order(BaseModel):
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    def __str__(self):
        return self.product.name