from django.contrib import admin
from presto.models import (
    InstructionLog,
    JsonDownloadInstruction,
)

admin.site.register(InstructionLog)
admin.site.register(JsonDownloadInstruction)
