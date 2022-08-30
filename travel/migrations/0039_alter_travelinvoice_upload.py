# Generated by Django 4.1 on 2022-08-24 19:46

from django.db import migrations, models

import travel.models


class Migration(migrations.Migration):
    dependencies = [
        ('travel', '0038_alter_travelinvoice_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinvoice',
            name='upload',
            field=models.FileField(blank=True, default=None, null=True, upload_to=travel.models.user_directory_path,
                                   validators=[travel.models.upload_validator]),
        ),
    ]
