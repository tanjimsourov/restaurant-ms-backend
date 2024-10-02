from sell import views
from django.urls import path

urlpatterns = [
    path('addfooditem', views.AddFoodItem.as_view(), name="addfooditem"),
    path('updatefooditem/<int:fooditem_id>/', views.UpdateFoodItemStatus.as_view(), name="UpdateFoodItem"),
    # path('addrestaurant', views.AddRestaurant.as_view(), name="addrestaurant"),
    # path('login', views.LoginAPIView.as_view(), name="login"),
]