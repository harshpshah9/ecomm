from django.urls import path
from .views import *
from product.views import *
app_name='custadmin'
urlpatterns = [
    path('',AdminDashboard.as_view(),name='admin_dashboard'),
    #category

    path('category/',CategoryListView.as_view(),name='category_list'),
    path('category/create',CategoryCreateView.as_view(),name='category_create'),
    path('category/update/<str:slug>', CategoryUpdateView.as_view(),name='category_update'),
    path('category/delete/<str:slug>', CategoryDeleteView.as_view(),name='category_delete'),
    
    #brand
    path('brand/',BrandListView.as_view(),name='brand_list'),
    path('brand/create',BrandCreateView.as_view(),name='brand_create'),
    path('brand/update/<str:slug>',BrandUpdateView.as_view(), name='brand_update'),
    path('brand/delete/<str:slug>',BrandDeleteView.as_view(), name='brand_delete'),

    #product
    path('product/create',ProductCreateView.as_view(),name='product_create'),
    path('product/',ProductListView.as_view(),name="product_list"),
    path('product/update/<str:slug>',ProductUpdateView.as_view(),name='product_update'),

    path('t',test.as_view(),name="testing")
]