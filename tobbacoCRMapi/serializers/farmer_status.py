from rest_framework import serializers

from ..models.farmer_status import FarmerStatus


class FarmerStatusSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FarmerStatus
        fields = '__all__'
