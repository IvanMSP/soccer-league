# Generated by Django 2.0.12 on 2019-03-23 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='picture',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='teams/picture/'),
        ),
    ]
