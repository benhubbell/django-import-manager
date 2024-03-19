import boto3
import json
import os
import requests
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotAllowed,
)
from django.template import loader
from presto.forms import JsonDownloadInstructionForm
from presto.models import JsonDownloadInstruction


api_key = 'zADOYxpraV1xPthfBAML41Fxhx1AT4ee8VCDWWAH'
aws_api_gateway = 'https://1gu5uk8gj5.execute-api.us-east-2.amazonaws.com/default/run-instruction-test'
headers = {'x-api-key': api_key}
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    # return HttpResponse("test")
    instruction_form_content = render_to_string('presto/partials/instruction_form_content.html')
    directory_form_input_group = render_to_string('presto/partials/directory_form_input_group.html')
    file_form_input_group = render_to_string('presto/partials/file_form_input_group.html')

    return render(request, 'presto/empty.html', {
        'instruction_form_content': instruction_form_content,
        'directory_form_input_group': directory_form_input_group,
        'file_form_input_group': file_form_input_group,
    })#, 'dirctory_form_element_group': directory_form_element_group})
    # return render(request, 'presto/index.html', {})
    instructions = JsonDownloadInstruction.objects.all()
    if request.method == 'POST':
        form = JsonDownloadInstructionForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            ftp_server_number = form.cleaned_data['ftp_server_number']
            instruction = form.cleaned_data['instruction']

            JsonDownloadInstruction.objects.create(
                client=client,
                ftp_server_number=ftp_server_number,
                instruction=instruction
            )
        else:
            return render(request, 'presto/empty.html', {'form': form, 'instructions': instructions})

    else:
        form = JsonDownloadInstructionForm()

    return render(request, 'presto/empty.html', {'form': form, 'instructions': instructions})
def index_old(request):
    instructions = JsonDownloadInstruction.objects.all()
    if request.method == 'POST':
        form = JsonDownloadInstructionForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            ftp_server_number = form.cleaned_data['ftp_server_number']
            instruction = form.cleaned_data['instruction']

            JsonDownloadInstruction.objects.create(
                client=client,
                ftp_server_number=ftp_server_number,
                instruction=instruction
            )
        else:
            return render(request, 'presto/index_old.html', {'form': form, 'instructions': instructions})

    else:
        form = JsonDownloadInstructionForm()

    return render(request, 'presto/index_old.html', {'form': form, 'instructions': instructions})

def start_download(request):

    if request.method != 'POST':
        return HttpResponse(status=405)

    json_download_instruction = JsonDownloadInstruction.objects.get(id=request.POST['instruction-id'])
    post_data = request.POST

    lambda_url = os.getenv('PPD_AWS_LAMBDA_URL')
    requests.post(lambda_url, {
        'PPD_CLIENT_ID': json_download_instruction.client,
        'PPD_FTP_SERVER_NUMBER': json_download_instruction.ftp_server_number,
        'PPD_INSTRUCTION_ID': json_download_instruction.id,
        'PPD_INSTRUCTIONS': json_download_instruction.instruction,
        'PPD_PRESTO_USERNAME': post_data['presto-username'],
        'PPD_PRESTO_PASSWORD': post_data['presto-password'],
    })

    return HttpResponse(json_download_instruction.instruction)
