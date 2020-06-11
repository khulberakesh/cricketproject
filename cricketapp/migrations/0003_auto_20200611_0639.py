# Generated by Django 2.0.4 on 2020-06-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0002_auto_20200611_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerhistory',
            name='score',
        ),
        migrations.AddField(
            model_name='playerhistory',
            name='high_score',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='High Score'),
        ),
    ]