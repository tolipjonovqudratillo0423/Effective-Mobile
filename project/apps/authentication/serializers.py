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
            "email",
            "password",
            "confirm_password",
        ]
        write_only_fields = [
            "confirm_password",
            "password"
        ]
        
        
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
        user = User.objects.create(
            username=None,
            **validated_data
        )
        return user
    



