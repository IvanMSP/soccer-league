# Generated by Django 2.0.12 on 2019-03-19 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(blank=True, max_length=25, null=True)),
                ('stature', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('sex', models.CharField(choices=[('femenino', 'Femenino'), ('masculino', 'Masculino')], default='Masculino', max_length=15)),
                ('number', models.IntegerField()),
                ('postion', models.CharField(choices=[('portero', 'Portero'), ('defensa', 'Defensa'), ('medio', 'Medio'), ('delantero', 'Delantero')], default='Ninguna', max_length=30)),
                ('team_player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
            },
        ),
    ]