# Generated by Django 4.2.1 on 2023-05-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_skills_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(blank=True, choices=[("Bachelor's degree", "Bachelor's degree"), ('Masters', 'Masters'), ('P.H.D', 'P.H.D')], max_length=50, null=True, verbose_name='مقطع'),
        ),
    ]