# Generated by Django 2.1.1 on 2019-02-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twengage', '0010_auto_20190226_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='follower_cnt',
            field=models.BigIntegerField(default=0, verbose_name='Follower Count'),
        ),
        migrations.AddField(
            model_name='account',
            name='following_cnt',
            field=models.BigIntegerField(default=0, verbose_name='Original Following Count'),
        ),
    ]
