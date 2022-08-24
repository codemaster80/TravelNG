# Generated by Django 4.1 on 2022-08-24 12:00

from django.db import migrations, models
import request.models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0037_alter_travelinvoice_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinvoice',
            name='upload',
            field=models.FileField(blank=True, default='no_file', null=True, upload_to=request.models.user_directory_path, validators=[request.models.upload_validator]),
        ),
    ]
