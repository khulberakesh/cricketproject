# Generated by Django 2.0.4 on 2020-06-11 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches', models.PositiveIntegerField(blank=True, null=True)),
                ('runs', models.PositiveIntegerField(blank=True, null=True, verbose_name='Runs')),
                ('wickets', models.PositiveIntegerField(blank=True, null=True, verbose_name='Wickets')),
                ('centuries', models.PositiveIntegerField(blank=True, null=True, verbose_name='Centuries')),
                ('fifties', models.PositiveIntegerField(blank=True, null=True, verbose_name='Fifties')),
                ('score', models.PositiveIntegerField(blank=True, null=True, verbose_name='Score')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('player_picture', models.URLField(blank=True, max_length=4096, null=True, verbose_name='Player Picture')),
                ('jersey_number', models.PositiveIntegerField(unique=True)),
                ('country', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
            ],
        ),
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logouri', models.URLField(max_length=4096, verbose_name='Logo')),
                ('club_state', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
            ],
        ),
        migrations.AddField(
            model_name='pointstable',
            name='team',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.PROTECT, related_name='team_points', to='cricketapp.Team'),
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_players', to='cricketapp.Team', verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='playerhistory',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player', to='cricketapp.Players', verbose_name='Players'),
        ),
        migrations.AddField(
            model_name='match',
            name='playing_team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playing_team1', to='cricketapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='playing_team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playing_team2', to='cricketapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='winner', to='cricketapp.Team'),
        ),
    ]