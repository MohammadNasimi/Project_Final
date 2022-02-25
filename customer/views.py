from django.shortcuts import render

from customer.permissions import IsOwnerPermission, IsSuperuserPermission
from customer.serializers import AddressSerializer, CustomerSerializer
from rest_framework import generics, permissions, authentication
from core.models import User
from customer.models import Address,Customer
import logging


# Create your views here.
class UserlistViewApi(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAdminUser, IsSuperuserPermission]
    # authentication_classes = [authentication.BasicAuthentication]


class UserDetailViewApi(generics.RetrieveAPIView):
    # log userDetailView
    logger = logging.getLogger('project.developers')
    logger.error("see user detail view ")

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsSuperuserPermission]
    # authentication_classes = [authentication.BasicAuthentication]


class AddresslistViewApi(generics.ListAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]

    # authentication_classes = [authentication.BasicAuthentication]

    def get_queryset(self):
        return Address.objects.filter(customer__user=self.request.user)


class AddressDetailViewApi(generics.RetrieveAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    # authentication_classes = [authentication.BasicAuthentication]
