from rest_framework import serializers
from apps.memories.models import Memory


class MemorySerializer(serializers.ModelSerializer):
    """
    Memory serializer used for both post and get requests.
    """

    posted_at = serializers.DateTimeField(format='on %D at %H:%M:%S', read_only=True)

    class Meta:
        model = Memory
        exclude = ('owner',)

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return Memory.objects.create(**validated_data)
