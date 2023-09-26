from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services.files_process_service import FilesProcessService
from .base import BaseListView


class FilesBaseDetailView(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get(self, pk: str) -> Response:
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def delete(self, pk: str) -> Response:
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilesBaseListView(BaseListView):
    model = None
    serializer_class = None
    file_service_class: FilesProcessService = None

    def post(self, request) -> Response:
        base64_data = request.data.get("base64_data")
        if not base64_data:
            return Response(
                {"errors": "File is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            serializer = self.serializer_class(
                data=self.file_service_class.store_file(request, base64_data)
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response(
                {"errors": str(e)}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
            )
