from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


#======================================================================
# Response Message
#======================================================================

class ResponseMessage:
    
    @staticmethod
    def success(
        message:str,
        data:dict
    ):
        
        return Response({
            "status":True,
            "message":message,
            "data":data
        }, status=status.HTTP_200_OK)

    
    @staticmethod
    def error(
        message:str,
        data:dict
    ):
        
        return Response({
            "status":False,
            "message":message,
            "data":data
        }, status=status.HTTP_400_BAD_REQUEST)

#======================================================================
# JWT TOKENS
#======================================================================

def tokens(
    user
)-> dict:
    
    refresh = RefreshToken.for_user(user=user)
    
    data = {
        'refresh_token': str(refresh),
        'access_token':str(refresh.access_token)
    }
    
    return data