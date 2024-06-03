from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import User
from users.otp import generateKey