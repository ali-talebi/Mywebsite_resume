# Generated by Django 4.2.1 on 2023-05-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=200, verbose_name='اسم دانشگاه')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='شروع ')),
                ('end', models.DateTimeField(auto_now_add=True, null=True, verbose_name='شروع ')),
                ('field', models.CharField(max_length=200, verbose_name='رشته')),
                ('avg', models.FloatField(verbose_name='معدل')),
                ('status', models.CharField(choices=[('end', 'پایان'), ('continue', 'در حال تحصیل')], max_length=10, verbose_name='وضعیت')),
            ],
        ),
    ]
