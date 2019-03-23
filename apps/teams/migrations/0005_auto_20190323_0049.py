# Generated by Django 2.0.12 on 2019-03-23 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_remove_stadium_teams'),
        ('teams', '0004_remove_team_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='league_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campo', to='league.League'),
        ),
        migrations.AddField(
            model_name='team',
            name='stadium_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campo', to='league.Stadium'),
        ),
    ]