# Generated by Django 4.1 on 2022-08-07 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_player_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerresponse',
            name='groupr2',
        ),
    ]
