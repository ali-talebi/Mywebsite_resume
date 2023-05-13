# Generated by Django 4.2.1 on 2023-05-12 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_education_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='end_update',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='شروع '),
        ),
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 15, 31, 23, 927883, tzinfo=datetime.timezone.utc), null=True, verbose_name='شروع '),
        ),
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 15, 31, 23, 927883, tzinfo=datetime.timezone.utc), null=True, verbose_name='شروع '),
        ),
    ]