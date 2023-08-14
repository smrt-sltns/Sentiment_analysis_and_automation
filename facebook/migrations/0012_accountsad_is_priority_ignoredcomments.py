# Generated by Django 4.2.2 on 2023-07-24 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facebook', '0011_creds_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsad',
            name='is_priority',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='IgnoredComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=250, null=True)),
                ('comment_id', models.CharField(max_length=100)),
                ('created_date', models.CharField(max_length=100)),
                ('ad_id', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
