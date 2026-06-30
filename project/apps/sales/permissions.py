from apps.authentication.permissions import HasPermission


#======================================================================
# Access Rules "Orders" Permissions
#======================================================================


class CanReadOrder(HasPermission):
    element = "order"
    action = "read"

class CanCreateOrder(HasPermission):
    element = "order"
    action = "create"

class CanUpdateOrder(HasPermission):
    element = "order"
    action = "update"

class CanDeleteOrder(HasPermission):
    element = "order"
    action = "delete"



#======================================================================
# Access Rules "Product" Permissions
#======================================================================


class CanReadProduct(HasPermission):
    element = "product"
    action = "read"

class CanCreateProduct(HasPermission):
    element = "product"
    action = "create"

class CanUpdateProduct(HasPermission):
    element = "product"
    action = "update"

class CanDeleteProduct(HasPermission):
    element = "product"
    action = "delete"

