from django.urls import path

from customer.views import UserlistViewApi, UserDetailViewApi, AddressDetailViewApi, AddresslistViewApi, \
    AddresscreateView, AddressUpdateView, AddressDeleteView,UpdateUserView

app_name = 'customer'
urlpatterns = [
    path('User_list/', UserlistViewApi.as_view(), name='User_list'),
    path('User_Detail/<int:pk>', UserDetailViewApi.as_view(), name='User_Detail'),
    path('User_update/<int:pk>', UpdateUserView.as_view(), name='User_update'),
    path('Address_list/', AddresslistViewApi.as_view(), name='Address_list'),
    path('Address_Detail/<int:pk>', AddressDetailViewApi.as_view(), name='Address_Detail'),
    path('Address_create/', AddresscreateView.as_view(), name='Address_create'),
    path('Address_update/<int:pk>', AddressUpdateView.as_view(), name='Address_update'),
    path('Address_delete/<int:pk>', AddressDeleteView.as_view(), name='Address_delete'),
]
