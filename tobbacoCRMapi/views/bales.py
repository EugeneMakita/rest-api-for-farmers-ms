from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.bales import Bales
from ..serializers.bales import BalesSerializer
from .base import BaseDetailView, BaseListView


class BalesDetail(BaseDetailView):
    """
    Bales Detail view.

    get:
    Retrieve a specific bales by id.

    patch:
    Update a specific bales by id.

    delete:
    Delete a specific bales by id.
    """
    model = Bales
    serializer_class = BalesSerializer

    @swagger_auto_schema(request_body=BalesSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class BalesList(BaseListView):
    """
    Contract List view.

    get:
    Retrieve a list of all bales.

    post:
    Create a new bales.
    """
    model = Bales
    serializer_class = BalesSerializer

    @swagger_auto_schema(request_body=BalesSerializer)
    def post(self, request) -> Response:
        return super().post(request)
