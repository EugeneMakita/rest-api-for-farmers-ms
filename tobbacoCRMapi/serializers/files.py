from rest_framework import serializers

from ..models.files import Files


class FilesSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Files
        fields = "__all__"
