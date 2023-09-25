from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.bales_qaulity import BalesQaulity
from ..serializers.bales_quality import BalesQaulitySerializer
from .base import BaseDetailView, BaseListView


class BalesQualityDetail(BaseDetailView):
    """
    Bales Quality Detail view.

    get:
    Retrieve a specific Qaulity by id.

    patch:
    Update a specific Qaulity by id.

    delete:
    Delete a specific Qaulity by id.
    """
    model = BalesQaulity
    serializer_class = BalesQaulitySerializer

    @swagger_auto_schema(request_body=BalesQaulitySerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class BalesQaulityList(BaseListView):
    """
    Bales  Qaulity List view.

    get:
    Retrieve a list of all Qaulities.

    post:
    Create a new Quality.
    """
    model = BalesQaulity
    serializer_class = BalesQaulitySerializer

    @swagger_auto_schema(request_body=BalesQaulitySerializer)
    def post(self, request) -> Response:
        return super().post(request)
