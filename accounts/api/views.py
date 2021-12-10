from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, logout, login
from rest_framework.authtoken.models import Token

from .serializers import (
    UserSerializer
)
User = get_user_model()
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    parsed_data = JSONParser().parse(request)
    print(parsed_data)
    serialized_data = UserSerializer(data=parsed_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)
    return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    json_data = JSONParser().parse(request)
    try:
        user = User.objects.get(email = json_data['username'])
    except Exception as e:
        return Response('Email is not existed')
    token = Token.objects.get_or_create(user=user)[0].key
    if not user.check_password(json_data['password']):
        return Response("Invalid password")
    data = {}
    if user:
        if user.is_active:
            print(user.get_full_name())
            data['email'] = user.get_full_name()
            login(request, user)
    response = {"data": data, "Token": token}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response("Logged out")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    users = User.objects.select_related('user').get(pk=request.user.id)
    print(users)
    serialized_users = UserSerializer(users)
    return Response(serialized_users.data, status=status.HTTP_200_OK)
