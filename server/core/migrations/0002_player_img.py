# Generated by Django 4.1 on 2022-08-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='img',
            field=models.URLField(blank=True, default='https://drive.google.com/uc?export=view&id=1f_Hr2NYr2XrecCxmIK23fNCLjsJo-ReQ'),
        ),
    ]
