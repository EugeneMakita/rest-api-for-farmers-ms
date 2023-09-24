from rest_framework import serializers

from ..models.contract import Contract


class ContractsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Contract
        fields = '__all__'
