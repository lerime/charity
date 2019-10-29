from rest_framework import viewsets

from app.faq.models import Faq
from app.faq.serializers import FaqSerializer


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
