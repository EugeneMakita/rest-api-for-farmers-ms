from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.farmer_status import FarmerStatus
from ..serializers.farmer_status import FarmerStatusSerializer
from .base import BaseDetailView, BaseListView


class FarmerStatusDetail(BaseDetailView):
    """
    Farmer Status Detail view.

    get:
    Retrieve a specific status by id.

    patch:
    Update a specific status by id.

    delete:
    Delete a specific status by id.
    """
    model = FarmerStatus
    serializer_class = FarmerStatusSerializer

    @swagger_auto_schema(request_body=FarmerStatusSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class FarmerStatusList(BaseListView):
    """
    Farmer Status List view.

    get:
    Retrieve a list of all status.

    post:
    Create a new status.
    """
    model = FarmerStatus
    serializer_class = FarmerStatusSerializer

    @swagger_auto_schema(request_body=FarmerStatusSerializer)
    def post(self, request) -> Response:
        return super().post(request)
