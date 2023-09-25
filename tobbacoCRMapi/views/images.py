from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

from ..helpers.image_processor import ImageProcessor
from ..models.images import Images
from ..serializers.images import ImagesSerializer
from .base import BaseListView

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ImageDetailView(APIView):
    """
    Images Detail view.

    get:
    Retrieve a specific images by id.

    delete:
    Delete a specific images by id.
    """

    def delete(self, pk):
        image = Images.objects.get(pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get(self, pk: str) -> Response:
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class ImagesList(BaseListView):
    """
    Images List view.

    get:
    Retrieve a list of all Images.

    post:
    Create a new Image.
    """
    model = Images
    serializer_class = ImagesSerializer

    @swagger_auto_schema(request_body=ImagesSerializer)
    def post(self, request) -> Response:
        base64_data = request.data.get('base64_data')
        if not base64_data:
            return Response({'errors': 'File is empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = ImagesSerializer(data=ImageProcessor.store_image(base64_data))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({'errors': str(e)}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
