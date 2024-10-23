from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

@api_view(["GET", "POST", "PUT", "DELETE"])
def ProductsView(request, pk=None):
    print(request.data)
    if request.method == "GET" and pk is None:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    if request.method == "GET" and pk is not None:
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

 
    if request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, sttatus=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT" and pk is not None:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, sttatus=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE" and pk is not None:
        print(request.data)
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)


    