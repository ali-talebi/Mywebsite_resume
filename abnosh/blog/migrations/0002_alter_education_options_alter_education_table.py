# Generated by Django 4.2.1 on 2023-05-12 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'تحصیلات'},
        ),
        migrations.AlterModelTable(
            name='education',
            table='Education',
        ),
    ]
