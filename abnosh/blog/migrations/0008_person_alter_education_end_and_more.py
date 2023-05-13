# Generated by Django 4.2.1 on 2023-05-12 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_education_end_update_alter_education_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم   ')),
                ('talebi', models.CharField(max_length=200, verbose_name=' اسم خانوادگی   ')),
                ('email', models.EmailField(max_length=200, verbose_name=' اسم خانوادگی   ')),
                ('phone', models.BigIntegerField(verbose_name='همراه شخصی ')),
                ('git_hub_slug', models.SlugField(max_length=200, verbose_name='آدرس گیت هاب    ')),
                ('Linkedin', models.SlugField(max_length=200, verbose_name='آدرس لینک دین ')),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 15, 38, 8, 838919, tzinfo=datetime.timezone.utc), null=True, verbose_name='پایان '),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_update',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='پایان '),
        ),
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 15, 38, 8, 838919, tzinfo=datetime.timezone.utc), null=True, verbose_name='شروع '),
        ),
    ]