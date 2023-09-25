from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.supplies import Supplies
from ..serializers.supplies import SuppliesSerializer
from .base import BaseDetailView, BaseListView


class SuppliesDetail(BaseDetailView):
    """
    Supplies Detail view.

    get:
    Retrieve a specific supplies by id.

    patch:
    Update a specific supplies by id.

    delete:
    Delete a specific supplies by id.
    """
    model = Supplies
    serializer_class = SuppliesSerializer

    @swagger_auto_schema(request_body=SuppliesSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class SuppliesList(BaseListView):
    """
    Supplies Detail view.

    get:
    Retrieve all supplies.

    post:
    Create a new supplies.
    """
    model = Supplies
    serializer_class = SuppliesSerializer

    @swagger_auto_schema(request_body=SuppliesSerializer)
    def post(self, request) -> Response:
        return super().post(request)
