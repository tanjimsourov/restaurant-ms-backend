# Generated by Django 5.0.6 on 2024-06-09 11:02

import accounts.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(default='', max_length=30, verbose_name='username')),
                ('restaurantName', models.CharField(default='', max_length=30, verbose_name='restaurantName')),
                ('restaurantAddress', models.CharField(default='', max_length=40, verbose_name='restaurantAddress')),
                ('ownerName', models.CharField(default='', max_length=30, verbose_name='ownerName')),
                ('nidNumber', models.CharField(default='', max_length=10, verbose_name='nid')),
                ('address', models.CharField(default='', max_length=50, verbose_name='address')),
                ('email', models.CharField(default='', max_length=50, null=True, verbose_name='email')),
                ('gender', models.CharField(default='', max_length=8, verbose_name='gender')),
                ('profilePic', models.ImageField(default='profilePic/default.jpg', upload_to=accounts.models.upload_to, verbose_name='Image')),
                ('phone', models.CharField(default=uuid.uuid1, max_length=11, unique=True)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('activation_key', models.CharField(blank=True, max_length=150, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('totalBal', models.FloatField(default=0)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_administrator', models.BooleanField(default=False, verbose_name='administrator')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('email_verified', models.BooleanField(default=False, verbose_name='email_verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.MyUserManager()),
            ],
        ),
    ]
