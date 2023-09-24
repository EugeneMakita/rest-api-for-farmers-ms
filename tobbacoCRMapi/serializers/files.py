from rest_framework import serializers

from ..models.images import Images


class ImagesSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Images
        fields = '__all__'