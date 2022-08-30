# Generated by Django 4.1 on 2022-08-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('travel', '0032_alter_travelinvoice_event_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinvoice',
            name='status',
            field=models.CharField(choices=[('In Prüfung', 'In Prüfung'), ('Genehmigt', 'Genehmigt')],
                                   default='In Prüfung', max_length=30),
        ),
        migrations.AlterField(
            model_name='travelinvoice',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='invoiceData/0a2ccca4-fb1d-4d43-a3a1-60c2ab159e8e'),
        ),
        migrations.AlterField(
            model_name='travelrequest',
            name='status',
            field=models.CharField(choices=[('In Prüfung', 'In Prüfung'), ('Genehmigt', 'Genehmigt')],
                                   default='In Prüfung', max_length=30),
        ),
    ]
