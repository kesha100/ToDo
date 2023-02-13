from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import MyUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=3, write_only=True)
    password_confirm = serializers.CharField(min_length=3, write_only=True)

    class Meta:
        model = MyUser
        fields = 'email password password_confirm'.split()

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError('Passwords do not match!')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        return user


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=3, write_only=True)

