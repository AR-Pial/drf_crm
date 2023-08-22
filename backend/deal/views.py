from rest_framework.viewsets import ModelViewSet

from .models import Opportunity,Document

from .serializers import OpportunitySerializer,DocumentSerializer

class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class OpportunityViewSet(ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer