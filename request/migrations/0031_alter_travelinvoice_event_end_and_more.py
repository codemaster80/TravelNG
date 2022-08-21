# Generated by Django 4.1 on 2022-08-16 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0030_alter_travelinvoice_event_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinvoice',
            name='event_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='event_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='journey_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='journey_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='invoiceData/58fbad8d-231e-423b-b991-7c2d5b3f5a5a'),
        ),
    ]