from django.shortcuts import render, redirect, HttpResponseRedirect
from . forms import HomeAwayForm, TeamForm, WinnerPickForm,WinnerSelectForm
from .models import Team, Home_Away,WinnerPick
from players import PLAYERS,Players # Players in the pool
from django.contrib.auth.decorators import login_required

# Add a new Team.
def teamform(request):
    form = TeamForm(request.POST or None)
            
    if form.is_valid():
        form.save()

        form = TeamForm()

    return render(request, 'teams/team.html', {'form': form})



def homeawayview(request):
    teams = Team.objects.all()
    form = HomeAwayForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HomeAwayForm()
        redirect('winner')

    else:
        form = HomeAwayForm()
        

    return render(request, 'teams/select_teams.html', {'form': form, 'teams': teams})

def print_final(request):
    winners=WinnerPick.objects.all()
    context = {
        "winners":winners,
        "players":PLAYERS
    }
    return render(request, 'teams/final.html',context)

def select_your_picks(request):
    pass

def winnerPick(request):  # Lets select the winner from a particular week
    if request.method == ('POST' or None):
        form=WinnerPickForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('select_week')
    else:
        form=WinnerPickForm()
    context={
        "form":form
    }
    
    return render(request,'teams/select_your_picks.html', context)

def winnerPick1(request):
    if request.method =='GET':
        week_number= request.GET['week_number']
        year = request.GET['year']
        player = request.GET['player']
        form= WinnerPickForm({'week_number':week_number,'year':year,'player':player})
    else:
        form=WinnerPickForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('select_week')
    context={
        'form':form
    }
    return render(request, 'teams/select_your_picks.html', context)
def total(request):
    pass

def print_winners(request):
    return render(request, 'teams/print_winners.html')

def printWeek(request,week_number  ):  # We also need to check the year.
    
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    total=home_aways.count()
    
     
    context = {
        'home_aways':home_aways,
        'week_number':week_number,
        'total':total       
       


    } 
    
           

    return render (request,'teams/print_week.html', context)


def select_winners(request):
   
    week_number=request.GET.get('week_number')
    player=request.GET.get('player')
    
    selections=Home_Away.objects.filter(week_number=week_number)
    
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    total=home_aways.count()
    form=WinnerPickForm()


    context = {
        
        'form':form,
        'week_number':week_number,
        'home_aways':home_aways,
        'total':total,
        
    
    }
    
    
      
    return render(request, 'teams/select_winners.html', context)    

def print_week(request):  # This function added 7/7/2023 to replace printweek function
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    
    
    
    context = {
        'home_aways':home_aways,
        'week_number':week_number,
         
        


    } 
    
           

    return render (request,'teams/print_week.html', context)



def confirm_selections(request):
    # List our selections from HomeAway and show an option 
    # to edit my choices.
    week_number=request.GET.get('week_number')
    year = request.GET.get('year') 
    #year = request.GET.get((year)
    selections=Home_Away.objects.filter(week_number=week_number)
    week_number=request.GET.get('week_number')
    home_aways = Home_Away.objects.filter(week_number=week_number).filter(startdate__year=year).order_by('startdate','starttime')
    
    # ______Lets find a way to determine the teams on a bye. _____________________________
    #_____________________________________________________________________________________

    context={
        'selections':selections,
        'week_number':week_number,
        'home_aways':home_aways,
        'year':year,
    }
    return render(request, 'teams/print_week.html',context)  

def pick_week(request):
    

    
    context = {
        "players":Players,


    }
    return render(request,'teams/pick_week.html', context)

def winnerPickList(request):
    list=WinnerPick.objects.all()
    return render(request,'teams/winnerPickList.html',{'list':list })

def save_winners(request):
    print('request', request)
    pick=request.GET.get('8')
    print('pick',pick)
    context={
        "pick":pick,

    }
    return render(request, 'teams/winners_saved.html',context)

@login_required
def winner_select_view(request):
    week_number=request.GET.get('week_number')
    print('week_number:',week_number)
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    
    
    print ('home_aways:',home_aways)
    #form=WinnerSelectForm()
    context={
        "teams":home_aways,
        #"form":form,

    }


    return render(request,'teams/select_winners.html',context)

def update(request, id):
    list = WinnerPick.objects.get(id=id)
    form = WinnerPickForm(instance = list)
    if request.method == ('POST' or None):
        if form.is_valid():
            form = WinnerPickForm(request.POST, instance=list)
            form.save()
            return HttpResponseRedirect('list')
    context = {
        'form':form,
        'list':list
    }    

    return render(request, 'teams/winnerPickUpdate.html', context)

