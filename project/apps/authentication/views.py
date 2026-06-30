from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.serializers import (
    RegisterSerializer,
    LoginSerializer
)
from apps.common.utils import (
    ResponseMessage,
    tokens
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



#======================================================================
# Login APIview
#======================================================================

class LoginAPIView(APIView):
    
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get("email", None)
        password = serializer.validated_data.get("password", None)
        
        user = authenticate(request, email=email, password=password)
        
        if not user:
            
            return ResponseMessage.error(
                message="User with this credentials not found!",
                data=serializer.data
            )
        
        return ResponseMessage.success(
            message=f"Welcome dear {user.username}!",
            data=tokens(user=user),
        )


#======================================================================
# Logout APIview
#======================================================================

class LogoutAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        refresh_token = request.data.get("refresh_token")
        
        if not refresh_token:
            return ResponseMessage.error(
                message="Refresh token required!",
            )
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return ResponseMessage.error(
                message="Invalid refresh token!"
            )
            
        return ResponseMessage.success(
            message="Logout successfully",
        )    
        

        
        


    