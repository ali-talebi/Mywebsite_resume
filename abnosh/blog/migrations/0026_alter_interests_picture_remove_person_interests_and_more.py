# Generated by Django 4.2.1 on 2023-05-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_interests_options_alter_interests_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interests',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='interests_picture', verbose_name='عکس علاقه مندی'),
        ),
        migrations.RemoveField(
            model_name='person',
            name='interests',
        ),
        migrations.AddField(
            model_name='person',
            name='interests',
            field=models.ManyToManyField(blank=True, null=True, to='blog.interests', verbose_name='علاقه مندی ها '),
        ),
    ]