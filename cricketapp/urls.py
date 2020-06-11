from django.urls import path
from django.conf.urls import url
from .views import TeamList,TeamInformationView,PointsTableView,MatchDetailsView,ScheduleMatch

app_name = 'cricketapp'

urlpatterns = [
    path('', TeamList.as_view(), name='team-list'),
    path('team-list/', TeamList.as_view(), name='team-list'),
    path('teaminfo/<int:team_id>/', TeamInformationView.as_view(), name="teaminfo"),
    path('pointstable/', PointsTableView.as_view(), name='pointstable'),
    path('matchdetails/', MatchDetailsView.as_view(), name='matchdetails'),
    path('schedule-match/', ScheduleMatch.as_view(), name='schedule-match'),
]