from rest_framework import serializers

from ..models.season_names import SeasonNames


class SeasonNamesSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SeasonNames
        fields = "__all__"
