from django.urls import path
from .views import *
# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'Authenticator', views.CameraInfoViewSet, basename="authenticator")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('authenticator/login/', LoginUserApi.as_view(), name='login'),
]
