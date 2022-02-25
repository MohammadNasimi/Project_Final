from rest_framework import serializers

from customer.models import Address,Customer
from core.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user', 'address_set']
    address_set = serializers.HyperlinkedRelatedField(view_name='customer:Address_Detail',queryset=Address.objects.all(), many=True)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    customer = CustomerSerializer(read_only=True)
