from rest_framework import serializers

from ..models.contact import Contact


class ContactSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
