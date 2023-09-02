from rest_framework.serializers import ModelSerializer

from .models import Opportunity, OpportunityDocument

class OpportunityDocumentSerializer(ModelSerializer):
    
     class Meta:
        model = OpportunityDocument  
        fields = '__all__'

class OpportunitySerializer(ModelSerializer):
   class Meta:
      model = Opportunity  
      fields = '__all__'
      read_only_fields = ('uuid',)