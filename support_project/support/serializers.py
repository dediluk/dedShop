from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    # Более 8 символов в пароле, не может быть прочитан пользователем
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # Нельзя отправлять токен вместе с запросом на регистрацию. Доступен только для чтения
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # Поля, которые могут быть в запросе/ответе
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Необходим email для входа.'
            )

        if password is None:
            raise serializers.ValidationError(
                'Необходим пароль для входа.'
            )


        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Данные для входа неверны.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Пользователь удален'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }