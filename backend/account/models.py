from django.db import models
from django.contrib.auth.models import User
import uuid


User._meta.get_field('email')._unique = True

class UserProfile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=30,null=True)
    department = models.CharField(max_length=30,null=True)
    designation = models.CharField(max_length=120,null=True)
    employee_id = models.CharField(max_length=100,null=True)
    types = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = 'user_profile'

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    
    



