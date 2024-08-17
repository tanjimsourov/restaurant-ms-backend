from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import User
from accounts.restaurantModel import Restaurant


class SuperUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password', 'token')
        read_only_fields = ['token']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class AdministratorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password', 'token')
        read_only_fields = ['token']

    def create(self, validated_data):
        return User.objects.create_administrator(**validated_data)


class AddRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'restaurant_address', 'restaurant_description', 'staff_count',
                  'manager_count', 'waiter_count', 'admin_count')


class AddRestaurantStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'full_name', 'address', 'nidNumber', 'connectedRestaurant', 'profilePic',
                  'gender', 'phone', 'is_verified', 'is_admin', 'is_manager', 'is_waiter', 'is_staff')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
