from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema


from apps.authentication.serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer
)
from apps.common.utils import (
    ResponseMessage,
    tokens
)

# Create your views here.



#======================================================================
# Register APIview
#======================================================================
@extend_schema(
    tags=["Auth"],
    summary="Register user."
)
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
@extend_schema(
    tags=["Auth"],
    summary="Login user."
)
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
            message=f"Welcome dear {user.first_name}!",
            data=tokens(user=user),
        )



#======================================================================
# Logout APIview
#======================================================================
@extend_schema(
    tags=["Auth"],
    summary="Logout user."
)
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
        

        
#======================================================================
# Profile APIview
#======================================================================
@extend_schema(
    tags=["Profile"],
    summary="User Profile."
)
class ProfileAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    
    def get(self, request):
        
        user = request.user
        
        return ResponseMessage.success(
            message="Your profile.",
            data={
                "profile":{
                    "first_name":user.first_name,
                    "middle_name":user.middle_name,
                    "last_name":user.last_name,
                    "email":user.email,
                }
            }
        )
    
    def put(self, request):
        
        instance = request.user
        
        serializer = self.serializer_class(
            data=request.data,
            instance=instance,
        )
        
        serializer.is_valid(raise_exception=True)
    
        serializer.save()
        
        return ResponseMessage.success(
            message="Profile updated.",
            data=serializer.data
        )
    def delete(self, request):
        
        user = request.user
        user.is_active = False
        user.save(update_fields=["is_active"])
        
        return ResponseMessage.success(
            message=f"Goodbye {user.first_name}😊 !"
        )


    