# Generated by Django 4.1.5 on 2023-05-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0008_alter_accountpages_longlived_access_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creds',
            name='has_ad_accounts',
            field=models.BooleanField(default=False),
        ),
    ]
