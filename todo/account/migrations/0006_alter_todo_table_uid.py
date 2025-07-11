# Generated by Django 5.1.5 on 2025-02-05 05:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_todo_table_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_table',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
