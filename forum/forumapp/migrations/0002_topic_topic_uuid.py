# Generated by Django 4.1.7 on 2023-03-25 16:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
