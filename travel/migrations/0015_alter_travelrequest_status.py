# Generated by Django 4.1 on 2022-08-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_alter_travelrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelrequest',
            name='status',
            field=models.CharField(choices=[('Wartet', 'Wartet'), ('Genehmigt', 'Genehmigt')], default='Wartet', max_length=30),
        ),
    ]