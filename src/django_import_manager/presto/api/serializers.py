from presto.models import JsonDownloadInstruction
from rest_framework import serializers
import json

class JsonDownloadInstructionSerializer(serializers.ModelSerializer):
    instruction = serializers.SerializerMethodField()

    class Meta:
        model = JsonDownloadInstruction
        fields = ['id', 'client', 'instruction']

    def get_instruction(self, obj):
        return json.loads(obj.instruction)
