# Generated by Django 4.2.1 on 2023-05-12 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_education_start_update_alter_education_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 15, 30, 21, 142995, tzinfo=datetime.timezone.utc), null=True, verbose_name='شروع '),
        ),
    ]