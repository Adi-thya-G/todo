# Generated by Django 5.1.5 on 2025-02-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_todo_table_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_table',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
