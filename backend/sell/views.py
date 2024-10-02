from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import response, status, permissions, viewsets
from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse
from sell.models import foodItem
from sell.serializers import (AddFoodItemSerializer, OrderSerializer, )
from django.db.models import Sum, Count
import csv


class AddFoodItem(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AddFoodItemSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.user.is_staff:
                serializer.save()
                return response.Response({'message': "Food Item Added Successfully!"}, status=status.HTTP_201_CREATED)
            return Response({'message': "You do not have fucking rights to create restaurant data!"},
                            status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateFoodItemStatus(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, id):
        foodObj = foodItem.objects.get(id=id)
        if foodObj:
            data = request.data
            foodObj.isAvailable = data["isAvailable"]
            foodObj.save()
            return Response(f"Status of Food Item with id: {id} has been updated", status=status.HTTP_201_CREATED)
        else:
            Response(f"Food item with id: {id} is not found", status=status.HTTP_404_NOT_FOUND)


class AddOrder(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.user.is_staff:
                serializer.save()
                return response.Response({'message': "Order Created Successfully!"}, status=status.HTTP_201_CREATED)
            return Response({'message': "You do not have fucking rights to create restaurant data!"},
                            status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
