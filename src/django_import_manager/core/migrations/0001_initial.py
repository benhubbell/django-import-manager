# Generated by Django 5.0.1 on 2024-02-26 19:04

import core.models
import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=500)),
                ('hashed_token', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=core.models.get_current_datetime_utc)),
                ('duration_in_minutes', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1440)])),
            ],
        ),
    ]