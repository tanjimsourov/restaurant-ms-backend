from accounts import views
from django.urls import path

urlpatterns = [
    path('superuser', views.SuperuserRegister.as_view(), name="superuser"),
    path('addrestaurant', views.AddRestaurant.as_view(), name="addRestaurant"),
    path('addreststaff', views.AddRestaurantEmployee.as_view(), name="addRestStaff"),
    path('employeelist', views.GetRestaurantEmployeeList.as_view(), name="GetRestaurantEmployeeList"),
    path('login', views.LoginAPIView.as_view(), name="login"),
]
