from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.contract_status import ContractStatus
from ..serializers.contracts_status import ContractsStatusSerializer
from .base import BaseDetailView, BaseListView


class ContractsStatusDetail(BaseDetailView):
    """
    Contact Status Detail view.

    get:
    Retrieve a specific contact by id.

    patch:
    Update a specific contact by id.

    delete:
    Delete a specific contact by id.
    """

    model = ContractStatus
    serializer_class = ContractsStatusSerializer

    @swagger_auto_schema(request_body=ContractsStatusSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class ContactsStatusList(BaseListView):
    """
    Contact Status List view.

    get:
    Retrieve a list of all contacts.

    post:
    Create a new contact.
    """

    model = ContractStatus
    serializer_class = ContractsStatusSerializer

    @swagger_auto_schema(request_body=ContractsStatusSerializer)
    def post(self, request) -> Response:
        return super().post(request)
