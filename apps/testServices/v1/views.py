from rest_framework import viewsets
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework import permissions
from common import generics_cursor
from .services import *
from datetime import datetime, timezone, timedelta

class TESTViewSet(viewsets.ViewSet):
    """
    Interact with TEST
    """
    permission_classes = [permissions.IsAuthenticated]

    # all swagger's parameters should be defined here 
    sw_page = openapi.Parameter(
        name='page', type=openapi.TYPE_STRING, namecription="Page number", in_=openapi.IN_QUERY)
    sw_size = openapi.Parameter(
        name='size', type=openapi.TYPE_STRING, namecription="Number of results to return per page", in_=openapi.IN_QUERY)
    sw_id = openapi.Parameter(
        name='id', type=openapi.TYPE_STRING,default='20221022000000000001', namecription="TEST id", in_=openapi.IN_QUERY)
    
    get_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_204_NO_CONTENT: 'NO_CONTENT',
        status.HTTP_200_OK: 'JSON',
    }
    post_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_200_OK: 'JSON',
    }
    put_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_200_OK: 'JSON',
    }
    delete_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_200_OK: 'JSON',
    }
    
    @swagger_auto_schema(method='get', manual_parameters=[sw_page, sw_size], responses=get_list_test_response)
    @action(methods=['GET'], detail=False, url_path='get-list-test')
    def get_list_test(self, request):
        """
        Get list service. If do not type input paramater, it will list all service
        input: None or id
        output: list test
        """
        try:
            page = request.query_params.get('page')
            size = request.query_params.get('size')
            condition_string = " WHERE test.id IS NOT NULL"
            param = []
            select_string = f"SELECT DISTINCT test.* FROM TEST.test"
            query_string = select_string + condition_string
            print(query_string)
            with connection.cursor() as cursor:
                obj = generics_cursor.getDictFromQuery(cursor, query_string, param, page, size)
                count = len(generics_cursor.getDictFromQuery(cursor, query_string, param,'1', '100000'))
            if obj is None:
                return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Error:", e)
            return Response(data={}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        return Response(data={"count": count, "data": obj}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(method='post', manual_parameters=[],request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, required=None,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, default='test'),
    }
    ),responses=post_list_test_response)
    @action(methods=['POST'], detail=False, url_path='post-add-test')
    def post_add_test(self, request):
        """
        Add a new service. You don't need type full param
        input: info of service
        output: True or False
        """
        dataDict=request.data
        try:
            name = dataDict.get('name')
            with connection.cursor() as cursor:
                param = [name]
                query_String =  f"INSERT INTO test(name) VALUES (%s)"
                print(query_String)
                print(param)
                cursor.execute(query_String, param)
                rows_affected=cursor.rowcount
                if rows_affected == 0:
                    cursor.close()
                    return Response(data={"result": False}, status=status.HTTP_304_NOT_MODIFIED)
                print("Add a row in TEST table")
        except Exception as e:
            print("Error: ", e)
            return Response(data={}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={"result": True}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(method='get', manual_parameters=[sw_id],
                         responses=get_list_test_response)
    @action(methods=['GET'], detail=False, url_path='get-test-info-by-id')
    def get_test_info_by_id(self, request):
        """
        Get test info by id
        input: id
        output: test info
        """
        try: 
            id=request.query_params.get('id')
            param=[id]
            select_string = f"SELECT test.* FROM TEST.test "
            condition_string = "id = %s "
            
            query_string = f"{select_string}  WHERE {condition_string} "
            print(query_string)
            obj = generics_cursor.getDictFromQuery(query_string,param)
            if obj is None:
                return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=obj, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(method='put', manual_parameters=[sw_id],request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, required=None,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, default='Thuế test')
    }
    ),responses=put_list_test_response)
    @action(methods=['PUT'], detail=False, url_path='put-change-info-test')
    def put_change_info_test(self, request):
        """
        Change info test by id. You don't need type full param
        input: info of test
        output: True or False
        """
        dataDict=request.data
        try:
            id = request.query_params.get('id')
            name = dataDict.get('name')
            with connection.cursor() as cursor:
                query_string = f"UPDATE test SET name = %s WHERE id = %s"
                param= [id, name]
                print (query_string)
                cursor.execute(query_string,param)
                rows_affected=cursor.rowcount
            if rows_affected == 0 :
                return Response(data={"result": False}, status=status.HTTP_304_NOT_MODIFIED)
        except Exception as e:
            print("err: ", e)
            return Response(data={}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={"result": True}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(method='delete', manual_parameters=[sw_id],
                         responses=delete_list_test_response)
    @action(methods=['DELETE'], detail=False, url_path='delete-remove-test')
    def delete_remove_test_by_id(self, request):
        """
        Delete test by id
        input: id test
        output: True or False
        """
        try: 
            id = request.query_params.get('id')
            with connection.cursor() as cursor:
                param=[id]                  
                query_string = f"DELETE FROM test WHERE id = %s" 
                cursor.execute(query_string,param)
                rows_affected=cursor.rowcount                     
            if rows_affected == 0 :
                return Response(data={"result": False}, status=status.HTTP_304_NOT_MODIFIED)
        except:
            return Response(data={}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={"result": True}, status=status.HTTP_200_OK)