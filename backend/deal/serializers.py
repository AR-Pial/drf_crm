from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Opportunity, OpportunityDocument

class OpportunityDocumentSerializer(ModelSerializer):
    
     class Meta:
        model = OpportunityDocument  
        fields = '__all__'

class OpportunitySerializer(ModelSerializer):
   manager_full_name = serializers.CharField(source='manager.profile.full_name', read_only=True)
   agent_full_name = serializers.CharField(source='agent.profile.full_name', read_only=True)
   class Meta:
      model = Opportunity  
      fields = '__all__'
      read_only_fields = ('uuid',)

   def update(self, instance, validated_data):
      for attr, value in validated_data.items():
         setattr(instance, attr, value)
      instance.save()
      return instance