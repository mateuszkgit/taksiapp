# Generated by Django 3.0.3 on 2020-02-04 20:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
