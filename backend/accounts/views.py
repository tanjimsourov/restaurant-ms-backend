from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate

from .models import User
# from .otp import generateKey
from .serializers import SuperUserSerializer, AddRestaurantSerializer


class SuperuserRegister(GenericAPIView):
    authentication_classes = []
    serializer_class = SuperUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if User.objects.filter(is_superuser=True).exists():
                return response.Response({'message': "You can't register for admin"},
                                         status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data['token'], status=status.HTTP_201_CREATED)
        else:
            return response.Response({"Fuck You"}, status=status.HTTP_200_OK)


class AddRestaurant(GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AddRestaurantSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.user.is_administrator:
                serializer.save()
                return Response({'message': "Restaurant Added Successfully!"}, status=status.HTTP_201_CREATED)
            return Response({'message': "You do not have fucking rights to create restaurant data!"},
                            status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
