from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.sales.repositories import (
    ProductRepository,
    OrderRepository,
)
from apps.sales.permissions import *
from apps.sales.serializers import (
    OrderSerializer,
    ProductSerializer
)
# Create your views here.



        
#======================================================================
# System APIview
#======================================================================
@extend_schema(
    tags=["Sales 'Products'."],
    summary="Product List | Create"
)
class ProductListCreateAPIView(ListCreateAPIView): 
    serializer_class = ProductSerializer
    queryset = ProductRepository.get_all()
    permission_classes = [
        IsAuthenticated,
    ] 
    
    permission_mapping = {
        'GET': [CanReadProduct],
        'POST': [CanCreateProduct],
    }
    def get_permissions(self):
        
        method = self.request.method.upper()
        
        if method in self.permission_mapping:
            return [perm() for perm in self.permission_mapping[method]]
        
        return super().get_permissions()




@extend_schema(
    tags=["Sales 'Products'."],
    summary="Product Retieve | Update | Delete."
)   
class ProductRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductRepository.get_all()
    permission_classes = [
        IsAuthenticated,
    ] 
    
    permission_mapping = {
        'GET': [CanReadProduct],
        'PUT': [CanUpdateProduct],
        'PATCH': [CanUpdateProduct],
        'DELETE': [CanDeleteProduct],
    }
    def get_permissions(self):
        
        method = self.request.method.upper()
        
        if method in self.permission_mapping:
            return [perm() for perm in self.permission_mapping[method]]
        
        return super().get_permissions()

   
   
   

#======================================================================
# System APIview
#======================================================================
@extend_schema(
    tags=["Sales 'Orders'."],
    summary="Order List | Create"
)
class OrderListCreateAPIView(ListCreateAPIView): 
    serializer_class = OrderSerializer
    queryset = OrderRepository.get_all()
    
    permission_classes = [
        IsAuthenticated,
    ] 
    
    permission_mapping = {
        'GET': [CanReadOrder],
        'POST': [CanCreateOrder],
    }
    def get_permissions(self):
        
        method = self.request.method.upper()
        
        if method in self.permission_mapping:
            return [perm() for perm in self.permission_mapping[method]]
        
        return super().get_permissions()




@extend_schema(
    tags=["Sales 'Orders'."],
    summary="Order Retieve | Update | Delete."
)   
class OrderRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = OrderRepository.get_all()

    permission_classes = [
        IsAuthenticated,
    ] 
    
    permission_mapping = {
        'GET': [CanReadOrder],
        'PUT': [CanUpdateOrder],
        'PATCH': [CanUpdateOrder],
        'DELETE': [CanDeleteOrder],
    }
    def get_permissions(self):
        
        method = self.request.method.upper()
        
        if method in self.permission_mapping:
            return [perm() for perm in self.permission_mapping[method]]
        
        return super().get_permissions()
