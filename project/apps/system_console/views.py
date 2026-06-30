from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.system_console.permissions import (
    IsAdmin
)
from apps.system_console.serializers import (
    BusinessElementSerializer,
    AccessRulesSerializer
)
from apps.system_console.repositories import (
    BusinessElementRepository,
    AccessRulesRepository
)

        
#======================================================================
# System APIview
#======================================================================
@extend_schema(
    tags=["System Elements"],
    summary="BE List | Create"
)
class BEListCreateAPIView(ListCreateAPIView):
    
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]  
    serializer_class = BusinessElementSerializer
    queryset = BusinessElementRepository.get_all()

@extend_schema(
    tags=["System Elements"],
    summary="BE Retieve | Update | Delete."
)   
class BERetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]  
    serializer_class = BusinessElementSerializer
    queryset = BusinessElementRepository.get_all()
    
   
   
   

#======================================================================
# System APIview
#======================================================================
@extend_schema(
    tags=["System Access Rules"],
    summary="AR List | Create"
)
class ARListCreateAPIView(ListCreateAPIView):
    
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]  
    serializer_class = AccessRulesSerializer
    queryset = AccessRulesRepository.get_all()

@extend_schema(
    tags=["System Access Rules"],
    summary="AR Retieve | Update | Delete."
)   
class ARRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]  
    serializer_class = AccessRulesSerializer
    queryset = AccessRulesRepository.get_all()
    
       
    
    