from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ..models.contact import Contact
from ..serializers.contacts import ContactSerializer
from .base import BaseDetailView, BaseListView


class ContactsDetail(BaseDetailView):
    """
    Contact Detail view.

    get:
    Retrieve a specific contact by id.

    patch:
    Update a specific contact by id.

    delete:
    Delete a specific contact by id.
    """
    model = Contact
    serializer_class = ContactSerializer

    @swagger_auto_schema(request_body=ContactSerializer)
    def patch(self, request, pk: str) -> Response:
        return super().patch(request, pk)


class ContactsList(BaseListView):
    """
    Contact List view.

    get:
    Retrieve a list of all contacts.

    post:
    Create a new contact.
    """
    model = Contact
    serializer_class = ContactSerializer

    @swagger_auto_schema(request_body=ContactSerializer)
    def post(self, request) -> Response:
        return super().post(request)
