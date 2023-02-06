from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'social_media_name', 'social_media_links', 'social_media_image_white', 'social_media_image', 'notes']