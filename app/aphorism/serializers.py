from rest_framework import serializers

from app.aphorism.models import Aphorism


class AphorismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aphorism
        fields = ('id', 'content', 'subtitle')
