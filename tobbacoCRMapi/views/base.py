from django.db import models
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseDetailView(APIView):
    model: models.Model = None
    serializer_class = None

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get(self, request: Request, pk: str) -> Response:
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def patch(self, request: Request, pk: str) -> Response:
        instance = self.get_object(pk)
        serializer = self.serializer_class(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BaseListView(APIView):
    model: models.Model = None
    serializer_class = None

    def get(self, request: Request) -> Response:
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
