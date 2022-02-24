from django.urls import path

from customer.views import UserlistViewApi ,UserDetailViewApi ,AddressDetailViewApi,AddresslistViewApi

app_name = 'customer'
urlpatterns = [
    path('User_list/', UserlistViewApi.as_view(), name='User_list'),
    path('User_Detail/<int:pk>', UserDetailViewApi.as_view(), name='User_Detail'),
    path('Address_list/', AddresslistViewApi.as_view(), name='Address_list'),
    path('Address_Detail/<int:pk>', AddressDetailViewApi.as_view(), name='Address_Detail'),
]
