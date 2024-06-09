from accounts import views
from django.urls import path

urlpatterns = [
     path('superuser', views.SuperuserRegister.as_view(), name="superuser"),
]