# Generated by Django 5.0.6 on 2024-07-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='page',
            field=models.IntegerField(default=0),
        ),
    ]
