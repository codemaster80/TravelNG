# Generated by Django 4.1 on 2022-09-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0042_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelrequest',
            name='supervisor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='supervisor',
            field=models.CharField(max_length=50),
        ),
    ]
