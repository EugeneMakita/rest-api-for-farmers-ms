from rest_framework import serializers

from ..models.season_workflows import SeasonWorkflows


class SeasonWorkflowsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SeasonWorkflows
        fields = '__all__'
