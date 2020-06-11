from django.contrib import admin
from django.core.exceptions import ValidationError

from cricketapp.models import Team,Players,PointsTable,Match,PlayerHistory


# Register your models here.




class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'logouri', 'club_state')

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team','image_uri', 'jersey_number', 'country')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('playing_team1', 'playing_team2', 'winner')

class PointsTableAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')

class PlayerHistoryAdmin(admin.ModelAdmin):
    list_display = ('player', 'matches', 'runs', 'wickets', 'centuries', 'fifties',
                    'high_score')


admin.site.register(Team,TeamAdmin)
admin.site.register(Players, PlayersAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(PointsTable, PointsTableAdmin)
admin.site.register(PlayerHistory, PlayerHistoryAdmin)