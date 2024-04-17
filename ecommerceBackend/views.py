from django.http import HttpResponse
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Documentation",
        default_version='v1',
        description="API documentation for your Django project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

def swagger_view(request):
    schema = schema_view.with_ui('swagger', cache_timeout=0)
    response = schema(request)
    response.render()  # Render the response content
    return response
