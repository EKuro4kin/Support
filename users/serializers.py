from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = ('id', 'username', 'first_name', 'last_name', 'role')


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.get('password')
        hashed_password = make_password(password)
        validated_data['password'] = hashed_password
        instance = super().create(validated_data)
        return instance

    class Meta:
        model = USER_MODEL
        fields = '__all__'
