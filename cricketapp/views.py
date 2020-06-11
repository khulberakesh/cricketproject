from django.shortcuts import render
from .models import Team,Players,PointsTable,Match
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#template view code start here
class TeamList(ListView):
    context_object_name = 'allteam'
    template_name = 'teamlist.html'
    model = Team


class TeamInformationView(ListView):
    template_name = 'team_info.html'
    model = Players

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players = context['object_list'].filter(team=self.kwargs['team_id'])
        context['teamdata'] = players
        context['team_name'] = players[0].team.name
        return context
     

class PointsTableView(ListView):
    template_name = 'pointstable.html'
    context_object_name = 'points'
    model = PointsTable


class MatchDetailsView(ListView):
    template_name = 'matchdetails.html'
    context_object_name = 'allmatch'
    model = Match

#template view code end here 
# =======================================================

#schedule match api code started
class ScheduleMatch(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            matchscheduler()
            return Response({"success": True, "message": 'MatchScheduled'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"is_success": False, "message": 'Not Scheduled'}, status=status.HTTP_400_BAD_REQUEST)


def matchscheduler():
	randamteam = Team.objects.order_by('?')[:2]
	if randamteam:
	    Match.objects.create(playing_team1=randamteam[0],playing_team2=randamteam[1],winner=None)

#schedule match api code started
