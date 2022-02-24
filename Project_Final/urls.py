"""Project_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from landing.views import HomeView
from product.views import product_list_api, category_list_api, productListApi, productDetailApi

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('landing.urls'), name='landing'),
    path('product/', include('product.urls'), name='product'),
    path('customer/', include('customer.urls'), name='customer'),
    # serializers
    # path('product/', product_list_api),
    # path('product_list/', productListApi.as_view()),
    # path('product_Detail/<int:pk>', productDetailApi.as_view()),
    # path('category/', category_list_api),
    prefix_default_language=True
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
