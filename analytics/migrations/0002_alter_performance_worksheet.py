# Generated by Django 4.0.4 on 2022-05-08 12:31

import analytics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='worksheet',
            field=models.FileField(upload_to=analytics.models._performance_upload_to, verbose_name='worksheet'),
        ),
    ]
