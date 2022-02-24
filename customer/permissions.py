from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSuperuserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer.user


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('user use', obj.customer.user)
        print('user', request.user)
        return request.user == obj.customer.user
