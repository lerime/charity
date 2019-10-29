from rest_framework import serializers

from app.faq.models import Faq


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'description', 'video_link', 'cover_photo_link', 'view_size')
