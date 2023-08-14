# Generated by Django 4.1.5 on 2023-05-23 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creds',
            name='ACCESS_TOKEN',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='creds',
            name='APP_ID',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='creds',
            name='APP_SECRET',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='creds',
            name='LONGLIVED_ACCESS_TOKEN',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='creds',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
