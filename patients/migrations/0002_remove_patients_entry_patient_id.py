# Generated by Django 2.1.5 on 2020-05-24 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients_entry',
            name='patient_id',
        ),
    ]
