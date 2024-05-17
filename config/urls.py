"""
URL configuration for code_base_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include,path,re_path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Swagger docs", # Standard
        default_version='v1.0', # Standard
        description="Swagger docs for Camera Management Services", 
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

prefix = 'test' # Standard

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(prefix + r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path(prefix + 'student/', include("apps.student_api.api.v1.urls")), # Standard
    path(prefix + '', include("apps.healthcheck.v1.urls")), # healthcheck Services
]
