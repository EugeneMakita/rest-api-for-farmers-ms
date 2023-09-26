from rest_framework import serializers

from ..models.land_type import LandType


class LandTypeSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = LandType
        fields = "__all__"
