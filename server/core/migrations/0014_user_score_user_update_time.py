# Generated by Django 4.1 on 2022-08-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_player_groupr2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
