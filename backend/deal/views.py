from rest_framework.viewsets import ModelViewSet
from .models import Opportunity,OpportunityDocument
from .serializers import OpportunitySerializer,OpportunityDocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


class OpportunityDocumentViewSet(ModelViewSet):
    queryset = OpportunityDocument.objects.all()
    serializer_class = OpportunityDocumentSerializer
    #permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('files[]')  # Get the list of uploaded files
        opportunity_id = request.data.get('opportunity')

        print(request.user)

        for file in files:
            serializer = self.get_serializer(data={
                'document': file,
                'opportunity': opportunity_id,
                'created_by': request.user.id,  # Assuming you want to associate the current user
            })
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response({'message': 'Files uploaded successfully'}, status=status.HTTP_201_CREATED)

class OpportunityViewSet(ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

    def create(self, request, *args, **kwargs):
        print("User : ",request.user)
        agent = request.data.get('agent')
        request.data._mutable = True
        if agent:
            request.data['stage'] = 'Assigned'
        request.data._mutable = False
        return super().create(request, *args, **kwargs)