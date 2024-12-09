from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Opportunity, OpportunityDocument, Proposal

class OpportunityDocumentSerializer(ModelSerializer):
    
     class Meta:
        model = OpportunityDocument  
        fields = '__all__'

class OpportunitySerializer(ModelSerializer):
   manager_full_name = serializers.CharField(source='manager.profile.full_name', read_only=True)
   agent_full_name = serializers.CharField(source='agent.profile.full_name', read_only=True)
   manager_user_id = serializers.CharField(source='manager.id', read_only=True)
   agent_user_id = serializers.CharField(source='agent.id', read_only=True)
   class Meta:
      model = Opportunity  
      fields = '__all__'
      read_only_fields = ('uuid',)

class ProposalSerializer(serializers.ModelSerializer):
      opportunity_name = serializers.CharField(source='opportunity.name', read_only=True)
      class Meta:
            model = Proposal
            fields = ['uuid', 'opportunity','opportunity_name', 'title', 'details', 'remarks'] 
            read_only_fields = ('uuid',)
      #    extra_kwargs = {
      #          'opportunity': {'required': False, 'allow_null': True},
      #          'created_by': {'required': False, 'allow_null': True},
      #    }
      def create(self, validated_data):
            # Automatically set the 'created_by' to the currently authenticated user
            user = self.context['request'].user  # Access the authenticated user
            validated_data['created_by'] = user  
            validated_data['modified_by'] = user  
            return super().create(validated_data)
