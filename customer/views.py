from django.shortcuts import render

from customer.permissions import IsOwnerPermission, IsSuperuserPermission
from customer.serializers import AddressSerializer, CustomerSerializer
from rest_framework import generics, permissions
from core.models import User
from customer.models import Address


# Create your views here.
class UserlistViewApi(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser, IsSuperuserPermission]


class UserDetailViewApi(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsSuperuserPermission]


class AddresslistViewApi(generics.ListAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Address.objects.filter(customer__user=self.request.user)


class AddressDetailViewApi(generics.RetrieveAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
