from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='profile.full_name', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name','full_name']