from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import JsonResponse


def root_view(request):
    return JsonResponse({"message": "Welcome to the Bridge Service API. Use /api/products/ to fetch products."})


schema_view = get_schema_view(
    openapi.Info(
        title="Bridge Service API",
        default_version='v1',
        description="A microservice to bridge clients and the Fake Store API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', root_view),  # Root endpoint
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
