from django.urls import path

from apps.sales.views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDelete,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDelete
)

urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(),name="product_lc"),
    path("products/<int:pk>/", ProductRetrieveUpdateDelete.as_view(),name="product_rud"),
    
    path("orders/", OrderListCreateAPIView.as_view(),name="order_lc"),
    path("orders/<int:pk>/", OrderRetrieveUpdateDelete.as_view(),name="order_rud"),
    
]