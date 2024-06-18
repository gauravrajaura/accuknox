from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'last_login', 'date_joined']
