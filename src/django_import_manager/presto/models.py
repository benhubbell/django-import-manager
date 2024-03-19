import json
import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
# from django.utils.translation import gettext_lazy as _

# def validate_directory(value):
#     if value == '/':
#         return
#     if not (value.startswith('/') and value.endswith('/')):
#         raise ValidationError('Directory must start and end with "/"')
#     for index in range(0, len(value)):
#         if value == '/' and value[index] == value[index + 1]:
#             raise ValidationError("Invalid Directory")
#             # raise ValidationError(_('%(value)'))

def validate_directory_and_file_json_array(value):
    try:
        instruction_dictionary = json.loads(value)
    except:
        raise ValidationError("Invalid JSON")
    print(type(instruction_dictionary) != dict)
    if type(instruction_dictionary) != dict:
        raise ValidationError("Instruction is not a dictionary")

    if "fileInstructions" not in instruction_dictionary:
        raise ValidationError("Missing key fileInstructions")
    
    if "boxscoreInstructions" not in instruction_dictionary:
        raise ValidationError("Missing key boxscoreInstructions")
    
# class FileDownloadInstruction(models.Model):
#     directory = models.CharField(max_length=500, validators=[validate_directory])
#     is_inclusive = models.BooleanField(default=False)
#     is_basic = models.BooleanField(default=False)
#     directories = models.CharField(max_length=500)
#     files = models.CharField(max_length=500)

# class BoxscoreDownloadInstruction(models.Model):
#     is_inclusive = models.BooleanField(default=False)

class JsonDownloadInstruction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.CharField(max_length=50)
    ftp_server_number = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    instruction = models.TextField(validators=[validate_directory_and_file_json_array])
    is_started = models.BooleanField(default=False)

class InstructionLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField()
    instruction = models.ForeignKey(JsonDownloadInstruction, on_delete=models.CASCADE)
