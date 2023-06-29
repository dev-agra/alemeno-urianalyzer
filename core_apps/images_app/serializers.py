from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for the image uploaded"""
    class Meta:
        model = Image
        fields = '__all__'
