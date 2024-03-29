# Generated by Django 4.1 on 2022-08-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('travel', '0031_alter_travelinvoice_event_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinvoice',
            name='event_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='event_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='journey_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='journey_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='invoiceData/5c89c8a8-216f-49b0-8524-e13924f8404f'),
        ),
    ]
