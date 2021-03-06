# Generated by Django 2.0.4 on 2020-06-11 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0003_auto_20200611_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='playing_team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playing_playing_playing_team1', to='cricketapp.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='playing_team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playing_playing_playing_team2', to='cricketapp.Team'),
        ),
    ]
