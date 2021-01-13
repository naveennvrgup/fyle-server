from django.db.models import fields
from rest_framework import serializers
from .models import Branches, Bank


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class AutoCompleteInputSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, max_length=100)
    limit = serializers.IntegerField(required=False)
    offset = serializers.IntegerField(required=False)
