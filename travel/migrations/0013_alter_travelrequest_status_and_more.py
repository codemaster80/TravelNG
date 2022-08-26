# Generated by Django 4.1 on 2022-08-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_alter_travelrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelrequest',
            name='status',
            field=models.CharField(choices=[('W', 'Wartet'), ('G', 'Genehmigt')], default='W', max_length=30),
        ),
        migrations.DeleteModel(
            name='TravelRequestStatus',
        ),
    ]