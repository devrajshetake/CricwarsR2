# Generated by Django 4.1 on 2022-08-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_player_dr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='dr',
            field=models.FloatField(default=0, verbose_name='Conditional Rating Change'),
        ),
    ]
