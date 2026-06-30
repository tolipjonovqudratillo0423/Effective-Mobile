from django.urls import path

from apps.sales.views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDelete,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDelete
)

urlpatterns = [
    path("product/", ProductListCreateAPIView.as_view(),name="product_lc"),
    path("product/<int:pk>/", ProductRetrieveUpdateDelete.as_view(),name="product_rud"),
    
    path("order/", OrderListCreateAPIView.as_view(),name="order_lc"),
    path("order/<int:pk>/", OrderRetrieveUpdateDelete.as_view(),name="order_rud"),
    
]