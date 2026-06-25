from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.authentication.serializers import (
    RegisterSerializer
)
from apps.common.utils import (
    ResponseMessage
)
# Create your views here.



#======================================================================
# Register APIview
#======================================================================

class RegisterAPIView(APIView):
    
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return ResponseMessage.success(
            message="User registered successfully",
            data=serializer.data
        )
    