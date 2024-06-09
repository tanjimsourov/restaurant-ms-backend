from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import User


class SuperUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password', 'token')
        read_only_fields = ['token']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
