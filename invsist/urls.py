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
from django.contrib import admin
from django.urls import path

# importando vistas
from inventory.views import BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView
from inventory.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from inventory.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from inventory.views import main

urlpatterns = [
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
    path('admin/', admin.site.urls),
    path('', main, name="main"),
]
