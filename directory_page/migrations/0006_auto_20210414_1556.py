# Generated by Django 3.1.7 on 2021-04-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory_page', '0005_auto_20210413_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons_subjects',
            name='subject',
        ),
        migrations.AddField(
            model_name='persons_subjects',
            name='subject_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
