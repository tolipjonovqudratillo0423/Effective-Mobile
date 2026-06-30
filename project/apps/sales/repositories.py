from apps.sales.models import (
    Order,
    Product
)

#======================================================================
# Order Repository
#======================================================================

class OrderRepository:
    
    @staticmethod
    def get_all():
        
        return (
            Order.objects
            .select_related(
                "product",
            )
            .filter(is_active=True)
        )
    
    

#======================================================================
# Product Repository
#======================================================================

class ProductRepository:
    
    @staticmethod
    def get_all():
        
        return Product.objects.filter(is_active=True)