from rest_framework.serializers import ModelSerializer

from .models import Opportunity, Document

class DocumentSerializer(ModelSerializer):
    
     class Meta:
        model = Document  
        fields = '__all__'

class OpportunitySerializer(ModelSerializer):
   documents = DocumentSerializer(many=True, required=False)

   class Meta:
      model = Opportunity  
      fields = '__all__'
      read_only_fields = ('uuid',)