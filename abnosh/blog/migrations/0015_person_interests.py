# Generated by Django 4.2.1 on 2023-05-13 09:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_skills_tools'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='interests',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='علاقه مندی ها '),
        ),
    ]
