from accounts import views
from django.urls import path

urlpatterns = [
     path('superuser', views.SuperuserRegister.as_view(), name="superuser"),
     path('addrestaurant', views.AddRestaurant.as_view(), name="addrestaurant"),
]