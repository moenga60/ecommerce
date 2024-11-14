from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import status
from products.models import Product

@api_view(['POST'])
def add_to_cart(request, product_id):
    quantity = int(request.data.get('quantity'))
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return Response({'message': 'item added to cart'}, status=status.HTTP_201_CREATED)
        
    else:
        
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id]['quantity'] += quantity
            
        else:
            cart[product_id] = {'quantity': quantity, 'product_id': product_id}

        request.session['cart'] = cart

        return Response({'message': 'item added to cart'}, status=status.HTTP_201_CREATED)





