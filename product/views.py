from django.shortcuts import render
from django.http import Http404, JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from product.serializers import ProductSerializer, CategorySerializer
from product.models import Product, Category
from rest_framework.response import Response
from rest_framework import generics


# @csrf_exempt
# def product_list_api(request):
#     if request.method == 'GET':
#         product_serializer = ProductSerializer(Product.objects.all(), many=True)
#         return JsonResponse({'data': product_serializer.data}, status=200)
#     elif request.method == 'POST':
#         data = request.POST
#         print('data:', data)
#         product_serializer = ProductSerializer(data=data)
#         if product_serializer.is_valid():
#             new_product = product_serializer.save()
#             # print(product_serializer.validated_data['new_product'])
#             return JsonResponse({'new_product_id': new_product.id}, status=201)
#         else:
#             return JsonResponse({'errors': product_serializer.errors}, status=400)
#     else:
#         return JsonResponse({}, status=405)


@api_view(['GET', 'POST'])
def product_list_api(request):
    if request.method == 'GET':
        product_serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response({'data': product_serializer.data}, status=200)
    elif request.method == 'POST':
        data = request.data
        print('data:', data)
        product_serializer = ProductSerializer(data=data)
        if product_serializer.is_valid():
            new_product = product_serializer.save()
            # print(product_serializer.validated_data['new_product'])
            return Response({'new_product_id': new_product.id}, status=201)
        else:
            return Response({'errors': product_serializer.errors}, status=400)
    else:
        return Response({}, status=405)


@api_view(['GET', 'POST'])
def category_list_api(request):
    if request.method == 'GET':
        category_serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response({'data': category_serializer.data}, status=200)
    elif request.method == 'POST':
        data = request.POST
        print('data:', data)
        category_serializer = CategorySerializer(data=data)
        if category_serializer.is_valid():
            new_category = category_serializer.save()
            # print(product_serializer.validated_data['new_product'])
            return Response({'new_product_id': new_category.id}, status=201)
        else:
            return Response({'errors': category_serializer.errors}, status=400)
    else:
        return Response({}, status=405)


class productListApi(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class productDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
