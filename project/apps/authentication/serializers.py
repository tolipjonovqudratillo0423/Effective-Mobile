from rest_framework import serializers

from apps.authentication.models import (
    User
)


#======================================================================
# Register Serializer
#======================================================================

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        
        model = User
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {
            "password":{
                "write_only":True
            },
            "confirm_password":{
                "write_only":True
            }
        }
        
        
    def validate(self, attrs):
        validated_data = super().validate(attrs)

        password = validated_data.get("password")
        confirm_password = validated_data.pop("confirm_password", None)
        # email = validated_data.
        if password != confirm_password:
            raise serializers.ValidationError(
                "Passwords don't match!"
            )
        
        return validated_data
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            username=None,
            password=password,
            **validated_data
        )
        return user
    

#======================================================================
# Login Serializer
#======================================================================

class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()


#======================================================================
# Profile Serializer
#======================================================================

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "middle_name",
            "last_name"
        ]
    
    def update(self, instance, validated_data):
        
        for attrs, param in validated_data.items():
            setattr(instance, attrs, param)
        instance.save()
        
        return instance
