# Generated by Django 4.2.1 on 2023-05-13 09:53

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_person_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='EXPERIENCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='جایگاه شغلی')),
                ('name_company', models.CharField(max_length=200, verbose_name='نام شرکت')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='شروع ')),
                ('start_update', models.DateTimeField(auto_now_add=True, null=True, verbose_name='شروع ')),
                ('end', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='پایان ')),
                ('end_update', models.DateTimeField(auto_now_add=True, null=True, verbose_name='پایان ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name_plural': 'تجربیات عملی ',
                'db_table': 'EXPERIENCE',
            },
        ),
    ]
