from accounts import views
from django.urls import path

urlpatterns = [
     path('adddps', views.AddDPS.as_view(), name="AddDPS"),
]