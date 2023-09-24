from rest_framework import serializers

from ..models.supplies_type import SuppliesType


class SuppliesTypeSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SuppliesType
        fields = '__all__'
