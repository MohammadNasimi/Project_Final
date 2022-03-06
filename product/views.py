from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from django.http import Http404, JsonResponse, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.views import View
from django.views.generic import ListView, DetailView

from order.models import Order_item
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


# class CategoryListview(View):
#
#     def get(self, request):
#         category_list = Category.objects.all()
#         context = {
#             'Category_list': category_list,
#         }
#         return render(request, 'landing/product/Category.html', context=context)


# class CategoryListview(View):
#     model = Category
#     template_name = 'landing/product/Category.html'
#     context_object_name = 'Category_list'


# class productListview(ListView):
#     model = Product
#     template_name = 'landing/product/List_product.html'
#     context_object_name = 'product_list'


class product_for_categoryListview(View):

    def get(self, request, pk):
        category_list = Category.objects.all()
        product_category = Product.objects.filter(category_id=pk)
        # paginator
        page = Paginator(product_category, 1)
        page_number = request.GET.get('page')

        product_category_page = page.page(page_number)

        # print(product_category)
        context = {
            'product_category_page': product_category_page,
            'Category_list': category_list,
            'cat_id': pk
        }
        return render(request, 'landing/product/List_product.html', context=context)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'Detail_product'
    # queryset = Product.objects.filter(id=pk)
    template_name = 'landing/product/Detail_view_product.html'


class add_to_OrderView(View):
    def post(self, request, pk):
        from product.Cart import Cart
        cart = Cart(request)
        cart.add(pk, request.POST['number'])
        # cart.__iter__()
        # print(len(cart))
        response = redirect('product:Detail_product', pk)
        response.set_cookie('count', len(cart))
        return response
