from rest_framework import serializers

from .models import User
from djoser.serializers import TokenSerializer
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'dob', 'role', 'dob', 'nationality', 'gender']


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password', 'gender', 'role', 'dob', 'nationality')

    def create(self, validated_data):
        """
        Sets user password.
        NOTE: Without this, User will never sign_in and password will not be encrypted
        """
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomTokenSerializer(TokenSerializer):
    """
    Override the djoser(https://djoser.readthedocs.io/en/latest/) token serializer
    Allows us to return user details along side the djoser token
    """
    auth_token = serializers.CharField(source='key')
    user = UserSerializer()

    class Meta:
        model = Token
        fields = (
            'auth_token', 'user'
        )
