from rest_framework import serializers

from ..models.farmer import Farmer


class FarmerSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Farmer
        fields = "__all__"
