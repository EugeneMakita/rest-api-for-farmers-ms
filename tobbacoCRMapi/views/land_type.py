from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.land_type import LandType
from ..serializers.land_type import LandTypeSerializer
from .base import BaseDetailView, BaseListView


class LandTypeDetail(BaseDetailView):
    """
    Land Type Detail view.

    get:
    Retrieve a specific land type by id.

    patch:
    Update a specific land type by id.

    delete:
    Delete a specific land type by id.
    """
    model = LandType
    serializer_class = LandTypeSerializer

    @swagger_auto_schema(request_body=LandTypeSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class LandTypeList(BaseListView):
    """
    Land Type List view.

    get:
    Retrieve a list of all Land Types.

    post:
    Create a new Land type.
    """
    model = LandType
    serializer_class = LandTypeSerializer

    @swagger_auto_schema(request_body=LandTypeSerializer)
    def post(self, request) -> Response:
        return super().post(request)
