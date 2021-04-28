# Generated by Django 3.1.7 on 2021-04-14 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory_page', '0023_delete_person_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person_subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='directory_page.subjects')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Person's subject",
                'verbose_name_plural': "Person's subjects",
            },
        ),
    ]