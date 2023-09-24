from rest_framework import serializers
from .models import SeasonNames

class SeasonNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonNames
        fields = '__all__'
