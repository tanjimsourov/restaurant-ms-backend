import uuid
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, UserManager, AbstractBaseUser)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from users.otp import generateKey


def upload_to(instance, filename):
    return 'profilePic/{filename}'.format(filename=filename)


class MyUserManager(UserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_verified', False)
        return self._create_user(username, password, **extra_fields)

    def create_administer(self, username, password=None, **extra_fields):

        if not password:
            raise ValueError("User must have a password")

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_administer', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):

        if not password:
            raise ValueError("User must have a password")

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_administer', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=30,
        default='',
        null=False
    )

    restaurantName = models.CharField(
        _('restaurantName'),
        max_length=30,
        default='',
        null=False
    )
    restaurantAddress = models.CharField(
        _('restaurantAddress'),
        max_length=40,
        default='',
        null=False
    )
    ownerName = models.CharField(
        _('ownerName'),
        max_length=30,
        default='',
        null=False
    )
    nidNumber = models.CharField(
        _('nid'),
        max_length=10,
        default='',
        null=False
    )
    dob = models.CharField(
        _('dob'),
        max_length=30,
        default='',
        null=False
    )
    location = models.CharField(
        _('location'),
        max_length=50,
        default='',
        null=False
    )
    email = models.CharField(
        _('email'),
        max_length=50,
        default='',
        null=True
    )
    gender = models.CharField(
        _('gender'),
        max_length=8,
        default='',
    )
    nominiName = models.CharField(
        _('nominiName'),
        max_length=30,
        default='',
    )
    nominiFname = models.CharField(
        _('nominiFname'),
        max_length=30,
        default='',
    )
    nominiMname = models.CharField(
        _('nominiMname'),
        max_length=30,
        default='',
    )
    nominidob = models.CharField(
        _('nominidob'),
        max_length=30,
        default='',
    )
    nominiRel = models.CharField(
        _('nominiRel'),
        max_length=15,
        default='',
    )

    profilePic = models.ImageField(
        _("Image"), upload_to=upload_to, default='profilePic/default.jpg')




    phone = models.CharField(max_length=11, blank=False, default=uuid.uuid1, unique=True)
    otp = models.IntegerField(null=True, blank=True)
    somiti_type = models.CharField(max_length=10, blank=True, null=True)
    activation_key = models.CharField(max_length=150, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_general = models.BooleanField(default=True)
    is_loanee = models.BooleanField(default=False)
    is_dps = models.BooleanField(default=False)
    is_fdr = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )

    totalBal = models.FloatField(default=0)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )

    is_admin = models.BooleanField(
        _('admin'),
        default=False,

    )

    is_administer = models.BooleanField(
        _('administer'),
        default=False,

    )
    created_at = models.DateField(auto_now_add=True)
    email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
    )
    objects = MyUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    @property
    def token(self):
        token = jwt.encode(
            {'username': self.username, 'email': self.email,
             'exp': datetime.utcnow() + timedelta(days=365)},
            settings.SECRET_KEY, algorithm='HS256')

        return token
