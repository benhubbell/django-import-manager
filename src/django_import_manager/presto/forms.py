from django.forms import ModelForm, CharField, PasswordInput
from django.utils.translation import gettext_lazy as _
from presto.models import JsonDownloadInstruction
from django.contrib.admin import ModelAdmin
from prettyjson import PrettyJSONWidget


class ClientLoginInfoForm():
    client_username = CharField(label='Client Username', max_length=50, required=True)
    client_password = CharField(max_length=50, widget=PasswordInput)

class JsonDownloadInstructionForm(ModelForm):

    class Meta:
        model = JsonDownloadInstruction
        fields = ['client', 'ftp_server_number', 'instruction']
        widgets = {
            'instruction': PrettyJSONWidget(),
        }
        labels = {
            'ftp_server_number': _('FTP Server Number')
        }

class JsonAdmin(ModelAdmin):
  form = JsonDownloadInstructionForm
