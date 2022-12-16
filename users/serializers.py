from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")] )
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"] == True:
            user = User.objects.create_superuser(**validated_data)
            return user

        user  = User.objects.create_user(**validated_data)
        return user
