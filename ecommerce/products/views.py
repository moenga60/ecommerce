from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

@api_view(["GET"])
def  get_product_list(request):
    products = Product.objects.all()    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_specific_product(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"message": "The specified product does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"message": "The product does not exist"}, status=status.HTTP_404_NOT_FOUND)



@api_view(["DELETE"])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
       

    