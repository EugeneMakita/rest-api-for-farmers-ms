from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.contract import Contract
from ..serializers.contracts import ContractsSerializer
from .base import BaseDetailView, BaseListView


class ContractsDetail(BaseDetailView):
    """
    Contract Detail view.

    get:
    Retrieve a specific contract by id.

    patch:
    Update a specific contract by id.

    delete:
    Delete a specific contract by id.
    """

    model = Contract
    serializer_class = ContractsSerializer

    @swagger_auto_schema(request_body=ContractsSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class ContractsList(BaseListView):
    """
    Contract List view.

    get:
    Retrieve a list of all contracts.

    post:
    Create a new contract.
    """

    model = Contract
    serializer_class = ContractsSerializer

    @swagger_auto_schema(request_body=ContractsSerializer)
    def post(self, request) -> Response:
        return super().post(request)
