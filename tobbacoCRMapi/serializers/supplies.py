from rest_framework import serializers

from ..models.supplies import Supplies


class SuppliesSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Supplies
        fields = "__all__"
