# Generated by Django 4.1 on 2022-08-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('travel', '0010_alter_travelrequest_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelrequeststatus',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
