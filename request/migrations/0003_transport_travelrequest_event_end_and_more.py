# Generated by Django 4.0.6 on 2022-07-31 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_alter_costcenter_cost_center_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='travelrequest',
            name='event_end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='travelrequest',
            name='event_start',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='travelrequest',
            name='journey_end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='travelrequest',
            name='journey_start',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='travelrequest',
            name='transport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.transport'),
        ),
    ]
