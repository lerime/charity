from rest_framework import viewsets

from app.aphorism.models import Aphorism
from app.aphorism.serializers import AphorismSerializer


class AphorismViewSet(viewsets.ModelViewSet):
    queryset = Aphorism.objects.all()
    serializer_class = AphorismSerializer
