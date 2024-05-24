from .models import Mail
from rest_framework import serializers


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ['id', 'email', 'subscribed_at']
        read_only_fields = ['id', 'subscribed_at']


