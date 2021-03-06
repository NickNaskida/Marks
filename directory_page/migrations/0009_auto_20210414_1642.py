# Generated by Django 3.1.7 on 2021-04-14 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory_page', '0008_auto_20210414_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons_subjects',
            name='user',
        ),
        migrations.AlterField(
            model_name='persons_subjects',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Add_subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ManyToManyField(to='directory_page.Subjects')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
