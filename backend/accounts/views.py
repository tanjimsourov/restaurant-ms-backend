from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate

from .models import User
# from .otp import generateKey
from .serializers import (SuperUserSerializer, AddRestaurantSerializer, AddRestaurantStaffSerializer ,
                          EmployeeDataSerializer)


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


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    def post(self, request):
        phone = request.data.get('phone', None)
        password = request.data.get('password', None)
        user = authenticate(username=phone, password=password)

        if user:
            return response.Response({"phone": user.phone, "username": user.username, "token": user.token},
                                     status=status.HTTP_200_OK)
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)


class AddRestaurantOwner(GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AddRestaurantStaffSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.user.is_administrator:
                serializer.save()
                return Response({'message': "Restaurant Owner added Successfully!"}, status=status.HTTP_201_CREATED)
            return Response({'message': "You do not have fucking rights to create restaurant data!"},
                            status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddRestaurantEmployee(GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AddRestaurantStaffSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.user.is_admin:
                serializer.save()
                return Response({'message': "Restaurant Employee added Successfully!"}, status=status.HTTP_201_CREATED)
            return Response({'message': "You do not have fucking rights to create restaurant data!"},
                            status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRestaurantEmployeeList(GenericAPIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        restID = request.user.connectedRestaurant
        model = User.objects.filter(connectedRestaurant=restID)
        serializer = EmployeeDataSerializer(model, many=True)
        return Response(serializer.data)
