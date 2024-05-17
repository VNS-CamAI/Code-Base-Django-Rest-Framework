from django.shortcuts import render
from common.generics import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from django.db import connection

class HealthcheckViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    
    
    get_list_healthcheck_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_204_NO_CONTENT: 'NO_CONTENT',
        status.HTTP_200_OK: 'JSON',
    }
    post_list_healthcheck_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_400_BAD_REQUEST: 'BAD_REQUEST',
        status.HTTP_200_OK: 'JSON',
    }

    @swagger_auto_schema(method='get', manual_parameters=[],
                         responses=get_list_healthcheck_response)
    @action(methods=['GET'], detail=False, url_path='get-healthcheck')
    def get_healthcheck(self, request):
        """
        Get healthcheck
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()                               
        except Exception as e:
            print(e)
            return Response(data={"result":"error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={"result":"ok"}, status=status.HTTP_200_OK)
        

    