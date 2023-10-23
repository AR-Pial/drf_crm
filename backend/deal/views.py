from rest_framework.viewsets import ModelViewSet
from .models import Opportunity,OpportunityDocument
from .serializers import OpportunitySerializer,OpportunityDocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.decorators import action
from django.http import JsonResponse, HttpResponse
import os


class OpportunityDocumentViewSet(ModelViewSet):
    queryset = OpportunityDocument.objects.all()
    serializer_class = OpportunityDocumentSerializer
    
    
    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('files[]')  # Get the list of uploaded files
        opportunity_id = request.data.get('opportunity')
        print("files",files)
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
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.document.path

        # Delete the file from the media folder
        if instance.document and os.path.exists(file_path):
            os.remove(file_path)

        # Delete the database record
        instance.delete()

        return Response(status=204)
    
    @action(detail=True, methods=['GET'], name='get_opportunity_documents')
    def get_opportunity_documents(self, request, *args, **kwargs):
        pk = kwargs['pk']
        opportunity = Opportunity.objects.filter(uuid=pk).first()
        documents = OpportunityDocument.objects.filter(opportunity=opportunity)
        # serialized_documents = list(documents.values())
        # return JsonResponse(serialized_documents,safe=False)
        serializer = self.get_serializer(documents, many=True)    
        return Response(serializer.data)
        

class OpportunityViewSet(ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    lookup_field = 'uuid'

    @action(detail=True, methods=['POST'], name='update_field')
    def update_field(self, request, *args, **kwargs):
        opportunity = self.get_object()
        print(opportunity)
        field_name = request.data.get('field_name')
        new_value = request.data.get('new_value')
        print("field_name : ",field_name)
        print("new_value : ",new_value)
        if hasattr(opportunity, field_name):
            setattr(opportunity, field_name, new_value)
            opportunity.save()
            serializer = self.get_serializer(opportunity)  # Pass the serializer class, not the model
            return Response(serializer.data)
        else:
            return Response({'detail': f'Field "{field_name}" does not exist on the Opportunity model.'}, status=status.HTTP_400_BAD_REQUEST)
    
    

    
    
    
    