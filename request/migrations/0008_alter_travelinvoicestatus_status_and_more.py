# Generated by Django 4.1 on 2022-08-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0007_travelinvoicestatus_travelrequeststatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinvoicestatus',
            name='status',
            field=models.CharField(default='wartet', max_length=30),
        ),
        migrations.AlterField(
            model_name='travelrequeststatus',
            name='status',
            field=models.CharField(default='wartet', max_length=30),
        ),
    ]
