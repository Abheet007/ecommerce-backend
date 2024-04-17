from django.urls import include, path
from rest_framework.routers import DefaultRouter

from product.views import ProductCategoryViewSet, ProductViewSet

app_name = "product"

router = DefaultRouter()
router.register(r"categories", ProductCategoryViewSet)
router.register(r"", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

