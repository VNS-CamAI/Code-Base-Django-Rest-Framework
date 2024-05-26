from rest_framework import permissions
from common import generics_cursor
from django.db import connection
from datetime import datetime, timezone, timedelta

class CustomPermissions(permissions.BasePermission):
    def __init__(self):
        super().__init__()
    
    def has_permission(self, request, view):
        try:
            if not (request.user and request.user.is_authenticated):
                return False
            username = request.user
            query_String=   "SELECT * FROM authenticatorServices_user WHERE is_superuser = 1 AND username = %s"
            param = [username]
            print(query_String)
            obj = generics_cursor.getDictFromQuery(query_String, param)
            if len(obj) > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Err: ", e)
            return False