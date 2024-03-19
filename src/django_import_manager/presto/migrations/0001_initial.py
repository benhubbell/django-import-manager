# Generated by Django 5.0.1 on 2024-02-26 19:04

import django.core.validators
import django.db.models.deletion
import presto.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JsonDownloadInstruction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client', models.CharField(max_length=50)),
                ('ftp_server_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('instruction', models.TextField(validators=[presto.models.validate_directory_and_file_json_array])),
                ('is_started', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InstructionLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presto.jsondownloadinstruction')),
            ],
        ),
    ]