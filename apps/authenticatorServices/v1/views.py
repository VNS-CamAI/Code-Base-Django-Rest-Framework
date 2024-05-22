
from rest_framework.views import APIView
from .serializers import CustomTokenObtainPairSerializer, LoginUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions,status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .services import *
from django.contrib.auth import authenticate
from rest_framework import exceptions
from common.generics import *

    
class LoginUserApi(APIView):
    permission_classes = [permissions.AllowAny]
     # all swagger's parameters should be defined here   
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, default='string'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, default='string'),
    }))    
    @action(methods=['POST'], detail=False, url_path='login')
    def post(self, request):
        print("start login")
        print(request.data)
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data # Fetch the data form serializer
        user = authenticate(username=data['username'], password=data['password']) # Authenticate the user     
        if not user:
            raise exceptions.AuthenticationFailed("Thông tin đăng nhập không chính xác!")
        # Generate Token
        refresh= CustomTokenObtainPairSerializer.get_token(user)
        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
            , status=status.HTTP_200_OK
            )
        