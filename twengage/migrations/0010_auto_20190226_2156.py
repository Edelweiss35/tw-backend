# Generated by Django 2.1.1 on 2019-02-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twengage', '0009_auto_20181007_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='follower_users',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Follower Users'),
        ),
        migrations.AddField(
            model_name='account',
            name='org_following_users',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Original Following Users'),
        ),
    ]
