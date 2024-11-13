from django.urls import path
from .views import  get_product_list, get_specific_product, create_product, update_product, delete_product, get_category_list, get_specific_category, create_category, update_category, delete_category

urlpatterns = [
    path('products/', get_product_list, name="all products" ),
    path('products/<uuid:pk>/', get_specific_product, name="specific product"),
    path('products/create/', create_product, name="create product"),
    path('products/<uuid:pk>/update/', update_product, name="update product"),
    path('products/<uuid:pk>/delete/', delete_product, name="delete product"),
    path('categories/', get_category_list, name="all categories"),
    path('categories/<uuid:pk>/', get_specific_category, name="specific category"),
    path('categories/create/', create_category, name="create category"),
    path('categories/<uuid:pk>/update/', update_category, name="update category"),
    path('categories/<uuid:pk>/delete/', delete_category, name="delete category"),
    
]
