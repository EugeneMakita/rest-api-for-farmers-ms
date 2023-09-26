from rest_framework import serializers

from ..models.season import Season


class SeasonSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Season
        fields = "__all__"
