from rest_framework import serializers

from ..models.contract_status import ContractStatus


class ContractsStatusSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ContractStatus
        fields = '__all__'
