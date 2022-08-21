# Generated by Django 4.1 on 2022-08-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0028_alter_travelinvoice_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelinvoice',
            name='event_end',
            field=models.DateTimeField(default='2022-01-01 08:00'),
        ),
        migrations.AddField(
            model_name='travelinvoice',
            name='event_start',
            field=models.DateTimeField(default='2022-01-01 08:00'),
        ),
        migrations.AddField(
            model_name='travelinvoice',
            name='journey_end',
            field=models.DateTimeField(default='2022-01-01 08:00'),
        ),
        migrations.AddField(
            model_name='travelinvoice',
            name='journey_start',
            field=models.DateTimeField(default='2022-01-01 08:00'),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='invoiceData/c695a71d-f3f3-4287-825a-404709099d7e'),
        ),
    ]