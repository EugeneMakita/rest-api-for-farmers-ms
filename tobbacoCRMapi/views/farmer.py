from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.farmer import Farmer
from ..serializers.farmer import FarmerSerializer
from .base import BaseDetailView, BaseListView


class FarmerDetail(BaseDetailView):
    """
    Farmer Detail view.

    get:
    Retrieve a specific farmer by id.

    patch:
    Update a specific farmer by id.

    delete:
    Delete a specific farmer by id.
    """

    model = Farmer
    serializer_class = FarmerSerializer

    @swagger_auto_schema(request_body=FarmerSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class FarmerList(BaseListView):
    """
    Farmer List view.

    get:
    Retrieve a list of all farmer.

    post:
    Create a new farmer.
    """

    model = Farmer
    serializer_class = FarmerSerializer

    @swagger_auto_schema(request_body=FarmerSerializer)
    def post(self, request) -> Response:
        return super().post(request)
