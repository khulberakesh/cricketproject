
# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import signals
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _




class Team(models.Model):
   #Team model contain details of cricket team

    name = models.CharField(null=False,blank=False,max_length=100)
    logouri = models.URLField(_('Logo'), blank=False,
                            null=False, max_length=4096)
    club_state = models.CharField(null=False,blank=False,max_length=100)
    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated date"), auto_now=True)


    def __str__(self):
        return self.name


class Players(models.Model):
    ''' Players model contain information of cricket players'''

    first_name = models.CharField(null=False,blank=False,max_length=100)
    last_name = models.CharField(null=True,blank=True,max_length=100)
    image_uri = models.URLField(_('Player Picture'),blank=True,
                              null=True, max_length=4096)
    jersey_number = models.PositiveIntegerField(unique=True,blank=False,null=False)
    country = models.CharField(null=False,blank=False,max_length=100)
    team = models.ForeignKey(Team, db_index=True, blank=True, null=True, related_name="team_players",verbose_name=_('Team'),on_delete=models.PROTECT)
    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated date"), auto_now=True)

    def __str__(self):
        return self.first_name


class PlayerHistory(models.Model):
    ''' PlayerHistory model contain details information of players cricket career'''

    player = models.ForeignKey(Players, db_index=True, blank=False, null=False, related_name="player",
                                verbose_name=_('Players'),on_delete=models.PROTECT)
    matches = models.PositiveIntegerField(blank=True,null=True)
    runs = models.PositiveIntegerField(_("Runs"),blank=True,null=True)
    wickets = models.PositiveIntegerField(_("Wickets"),blank=True,null=True)
    centuries = models.PositiveIntegerField(_("Centuries"),blank=True,null=True)
    fifties = models.PositiveIntegerField(_("Fifties"),blank=True,null=True)
    high_score = models.PositiveIntegerField(_("High Score"),blank=True,null=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)


class Match(models.Model):
    ''' Match model contain match details '''
    playing_team1 = models.ForeignKey(Team, db_index=True, blank=False, null=False, related_name="playing_playing_playing_team1",on_delete=models.PROTECT)
    playing_team2 = models.ForeignKey(Team, db_index=True, blank=False, null=False, related_name="playing_playing_playing_team2",on_delete=models.PROTECT)
    winner = models.ForeignKey(Team, db_index=True, blank=True, null=True, related_name="winner",on_delete=models.PROTECT)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at= models.DateTimeField(_("updated_at"), auto_now=True)

    def save(self, *args, **kwargs):
        if self.playing_team1 is not None and (self.winner == self.playing_team2 or self.winner == self.playing_team2):
            super().save(*args, **kwargs)
        elif self.winner is None:
            super().save(*args, **kwargs)
        else:
            raise ValidationError(u'Please enter a valid team')


class PointsTable(models.Model):
    ''' PointsTable model contain points collected by cricket teams '''

    team = models.OneToOneField(Team, max_length=50, related_name='team_points',on_delete=models.PROTECT)
    points = models.PositiveIntegerField(default=0)


def save_points(sender, instance, created,update_fields, **kwargs):
    if not created:
        team = get_object_or_404(PointsTable, team=instance.winner)
        team.points +=2
        team.save()

"""Signal to save points of the winning team"""

signals.post_save.connect(receiver=save_points, sender=Match)



