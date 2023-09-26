from rest_framework import serializers

from ..models.bales_qaulity import BalesQaulity


class BalesQaulitySerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BalesQaulity
        fields = "__all__"
