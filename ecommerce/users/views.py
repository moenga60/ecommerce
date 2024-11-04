from rest_framework.response  import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(["POST"])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        return Response({
            "message": "Login successful",
            "user": user_serializer.data,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Username or password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def user_register(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Registered successfully"}, status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response({"message":"Logout successfully"})