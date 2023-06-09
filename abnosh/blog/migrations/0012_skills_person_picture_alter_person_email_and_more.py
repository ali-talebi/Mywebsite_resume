# Generated by Django 4.2.1 on 2023-05-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_person_educations_alter_education_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='skills', verbose_name=' عکس مهارت ')),
                ('name', models.CharField(max_length=30, verbose_name='مهارت')),
                ('applications', models.TextField(verbose_name='کاربرد ها ')),
                ('level', models.CharField(choices=[('1', 'حرفه ای '), ('2', 'متخصص'), ('3', 'مبتدی'), ('4', 'متوسط')], max_length=30, verbose_name='سطح مهارت')),
                ('tools', models.CharField(max_length=200, verbose_name='ابزار ها ')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='Image_person', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='ایمیل  '),
        ),
        migrations.AddField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(to='blog.skills'),
        ),
    ]
