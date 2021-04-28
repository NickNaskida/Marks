# Generated by Django 3.1.7 on 2021-04-14 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory_page', '0012_auto_20210414_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons_subjects',
            name='subject',
        ),
        migrations.AddField(
            model_name='persons_subjects',
            name='subject',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='directory_page.subjects'),
        ),
    ]