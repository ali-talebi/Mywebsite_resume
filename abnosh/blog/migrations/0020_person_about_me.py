# Generated by Django 4.2.1 on 2023-05-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_person_linkedin_alter_person_git_hub_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='about_me',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='درباره من '),
        ),
    ]
