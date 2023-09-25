from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.supplies_type import SuppliesType
from ..serializers.supplies_type import SuppliesTypeSerializer
from .base import BaseDetailView, BaseListView


class SuppliesTypeDetail(BaseDetailView):
    """
    Supplies Type Detail view.

    get:
    Retrieve a specific supplies type by id.

    patch:
    Update a specific supplies type by id.

    delete:
    Delete a specific supplies type by id.
    """
    model = SuppliesType
    serializer_class = SuppliesTypeSerializer

    @swagger_auto_schema(request_body=SuppliesTypeSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class SuppliesTypeList(BaseListView):
    """
    Supplies Type Detail view.

    get:
    Retrieve all supplies type.

    post:
    Create a new supplies type.
    """
    model = SuppliesType
    serializer_class = SuppliesTypeSerializer

    @swagger_auto_schema(request_body=SuppliesTypeSerializer)
    def post(self, request) -> Response:
        return super().post(request)
