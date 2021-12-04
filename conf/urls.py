"""invsist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from inventory.views import (BrandCreateView, BrandDeleteView, BrandListView,
                             BrandUpdateView, CategoryCreateView,
                             CategoryDeleteView, CategoryListView,
                             CategoryUpdateView, ProductCreateView,
                             ProductDeleteView, ProductListView,
                             ProductUpdateView, main)
# importando vistas
from store.views import (BuyerCreateView, BuyerDeleteView, BuyerListView,
                         BuyerUpdateView, OrderCreateView, OrderListView, OrderUpdateView,
                         SupplierCreateView, SupplierDeleteView,
                         SupplierListView, SupplierUpdateView)

from core.views import UserCreateView, UserListView, UserUpdateView

urlpatterns = [
    # supplier
    path('store/supplier/<int:pk>/delete', SupplierDeleteView.as_view(), name="supplier_delete"),
    path('store/supplier/<int:pk>/update', SupplierUpdateView.as_view(), name="supplier_update"),
    path('store/supplier/add', SupplierCreateView.as_view(), name="supplier_create"),
    path('store/supplier', SupplierListView.as_view(), name="supplier_list"), 
    # store
    path('store/buyer/<int:pk>/delete', BuyerDeleteView.as_view(), name="buyer_delete"),
    path('store/buyer/<int:pk>/update', BuyerUpdateView.as_view(), name="buyer_update"),
    path('store/buyer/add', BuyerCreateView.as_view(), name="buyer_create"),
    path('store/buyer', BuyerListView.as_view(), name="buyer_list"), 
    # order
    path('store/order', OrderListView.as_view(), name="order_list"), 
    path('store/order/add', OrderCreateView.as_view(), name="order_create"),
    path('store/order/<int:pk>/update', OrderUpdateView.as_view(), name="order_update"),
    # product
    path('inventory/products/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('inventory/products/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),
    path('inventory/products/add', ProductCreateView.as_view(), name="product_create"),
    path('inventory/products', ProductListView.as_view(), name="product_list"),
    # category
    path('inventory/categories/<int:pk>/delete', CategoryDeleteView.as_view(), name="category_delete"),
    path('inventory/categories/<int:pk>/update', CategoryUpdateView.as_view(), name="category_update"),
    path('inventory/categories/add', CategoryCreateView.as_view(), name="category_create"),
    path('inventory/categories', CategoryListView.as_view(), name="category_list"),
    # brand
    path('inventory/brands/<int:pk>/delete', BrandDeleteView.as_view(), name="brand_delete"),
    path('inventory/brands/<int:pk>/update', BrandUpdateView.as_view(), name="brand_update"),
    path('inventory/brands/add', BrandCreateView.as_view(), name="brand_create"),
    path('inventory/brands', BrandListView.as_view(), name="brand_list"),
    path('accounts/users/<int:pk>/update', UserUpdateView.as_view(), name="user_update"),
    path("accounts/users/add", UserCreateView.as_view(), name="user_create"),
    path("accounts/users", UserListView.as_view(), name="user_list"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', main, name="main"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
