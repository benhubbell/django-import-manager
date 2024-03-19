from presto.models import JsonDownloadInstruction
from presto.api.serializers import JsonDownloadInstructionSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import HttpResponse
import requests
import json
from presto.models import (
    InstructionLog,
    JsonDownloadInstruction,
)
class JsonDownloadInstructionViewSet(viewsets.ModelViewSet):
    queryset = JsonDownloadInstruction.objects.all()
    serializer_class = JsonDownloadInstructionSerializer

@api_view(['POST'])
def log_test(request):
    print("here")
    print("here")
    print("here")
    print("here")
    print("here")
    print("here")
    print("here")
    print("here")
    print("here")
    print(request.headers)
    # print(request.body)

    message_type = request.headers['X-Amz-Sns-Message-Type']
    # If message type is Subscription Confirmation, visit url to confirm
    if message_type == 'SubscriptionConfirmation':
        requests.get(json.loads(request.body.decode('utf-8'))['SubscribeURL'])
        # requests.get()
    elif message_type == 'Notification':
        body = json.loads(request.body.decode('utf-8'))
        JsonDownloadInstruction.objects.filter()

    return HttpResponse('good')