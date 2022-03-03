from django.shortcuts import render
from django.views import View
from customer.forms import AddressForm
from customer.permissions import IsOwnerPermission, IsSuperuserPermission
from customer.serializers import AddressSerializer, CustomerSerializer
from rest_framework import generics, permissions
from customer.models import Address, Customer
import logging
from rest_framework import renderers
from django.contrib import messages


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
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = 'landing/customer/customer_page.html'


class AddresslistViewApi(generics.ListAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]

    # authentication_classes = [authentication.BasicAuthentication]

    def get_queryset(self):
        return Address.objects.filter(customer__user=self.request.user)

    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = 'landing/customer/address_customer.html'


class AddressDetailViewApi(generics.RetrieveAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    # authentication_classes = [authentication.BasicAuthentication]


# class AddresscreateViewApi(generics.CreateAPIView):
#     serializer_class = AddressSerializer
#     queryset = Address.objects.all()
#     permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]

# class AddresscreateViewApi(View):
#     renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
#     template_name = 'landing/customer/address_customer.html'
#
#     def get(self, request):
#         render(request, 'landing/customer/address_customer.html')
#
#     def post(self, request):
#         data = request.data
#         print('data:', data)
#         Address_serializer = AddressSerializer(data=data)
#         if Address_serializer.is_valid():
#             # new_product = Address_serializer.save()
#             print(Address_serializer.validated_data['new_product'])
#             return render(request, 'landing/customer/address_customer.html')
#         else:
#             return render(request, 'landing/customer/address_customer.html')

# class AddresscreateViewApi(CreateView):
#     model = Address
#     fields = '__all__'
#     template_name = 'landing/customer/create_Address.html'
#     success_url = reverse_lazy('customer:Address_create')

class AddresscreateView(View):
    form_class = AddressForm
    template_name = 'landing/customer/create_Address.html'

    def get(self, request):
        return render(request, 'landing/customer/create_Address.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            province = request.POST["province"]
            city = request.POST["city"]
            town = request.POST["town"]
            street = request.POST["street"]
            alley = request.POST["alley"]
            Plaque = request.POST["Plaque"]
            zip_code = request.POST["zip_code"]
            id_user = self.request.user.id
            customer = Customer.objects.get(user_id=id_user)
            address_new = Address.objects.create(province=province, city=city, town=town, street=street, alley=alley,
                                                 Plaque=Plaque
                                                 , zip_code=zip_code, customer=customer)
            address_new.save()
            messages.add_message(request, messages.ERROR, "create success")
            return render(request, 'landing/customer/create_Address.html', {'form': self.form_class})
        messages.add_message(request, messages.ERROR, "zip code use before")
        return render(request, 'landing/customer/create_Address.html', {'form': self.form_class})