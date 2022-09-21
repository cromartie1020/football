from django.shortcuts import render
from .models import Team
# Create your views here.
def index(request):
    teams=Team.objects.all().order_by('location')
    context={
        'teams':teams
    }    
    print (teams)
    return render(request,'teams/home_away.html',context)