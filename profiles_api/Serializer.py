from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Searilizer a name field for testing our API View"""

    name=serializers.CharField(max_length=10)