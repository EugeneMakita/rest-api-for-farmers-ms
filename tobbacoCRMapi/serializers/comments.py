from rest_framework import serializers

from ..models.comments import Comments


class CommentsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'
