from rest_framework import permissions, viewsets

from product.models import Product, ProductCategory
# from product.permissions import IsSellerOrAdmin
from product.serializers import (
    ProductCategoryReadSerializer,
    ProductReadSerializer,
    ProductWriteSerializer,
)


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve product categories
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryReadSerializer
    permission_classes = (permissions.AllowAny,)


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD products
    """

    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ProductWriteSerializer

        return ProductReadSerializer

    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.AllowAny,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (permissions.AllowAny,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()