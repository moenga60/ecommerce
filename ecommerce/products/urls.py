from django.urls import path
from .views import  get_product_list, get_specific_product, create_product, update_product, delete_product

urlpatterns = [
    path('products/', get_product_list, name="all products" ),
    path('products/<uuid:pk>/', get_specific_product, name="specific product"),
    path('products/create/', create_product, name="create product"),
    path('products/<uuid:pk>/update/', update_product, name="update product"),
    path('products/<uuid:pk>/delete/', delete_product, name="delete product"),
]
