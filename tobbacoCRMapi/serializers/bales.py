from rest_framework import serializers

from ..models.bales import Bales


class BalesSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Bales
        fields = "__all__"
