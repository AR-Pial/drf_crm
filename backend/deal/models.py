from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Opportunity(models.Model):
    STAGE_CHOICES = [
        ('Unassigned', 'Unassigned'),
        ('Assigned', 'Assigned'),
        ('Successful', 'Successful'),
        ('Unsuccessful', 'Unsuccessful'),
    ]
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'agent'},related_name="agent_opportunity")
    manager = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'manager'},related_name="manager_opportunity")
    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=25,default="Unassigned")
    company_name = models.TextField(null=True)
    company_details = models.TextField(null=True)
    project_details = models.TextField(null=True)
    contact_details = models.TextField(null=True)
    additional_info = models.TextField(null=True)
    
    class Meta:
        db_table = "opportunities"


class OpportunityDocument(models.Model):
    document = models.FileField(upload_to='project_docs/', null=True)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name="opportunity_docs")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="documents")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "opportunity_documents"
    
    
class OpportunityComment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    comment = models.TextField()
    created_by = models.OneToOneField(User, on_delete=models.CASCADE,related_name="created_opportunity_comment")
    modified_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True,related_name="modified_opportunity_comment")
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "opportunity_comments"

    
    
