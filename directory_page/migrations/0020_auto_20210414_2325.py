# Generated by Django 3.1.7 on 2021-04-14 19:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory_page', '0019_auto_20210414_2320'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users_subjects',
            new_name='Persons_subjects',
        ),
    ]