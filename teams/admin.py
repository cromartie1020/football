from django.contrib import admin
from .models import Team, Home_Away,WinnerPick


class Home_Away_Form(admin.ModelAdmin):
    list_display = ['week_number','startdate','away_team','home_team', 'starttime']
    list_editable = ['startdate','away_team','home_team', 'starttime']
    search_fields =['week_number']
    list_per_page =16
class WinnerPickForm(admin.ModelAdmin):
    list_display=['week_number','year','player','away','home','away_score','home_score','selected_pick','actual_winner','status'] 
    list_editable=['away','home','away_score','home_score','selected_pick','actual_winner','status']
    search_fields=['week_number','year','away','home']
    list_per_page = 18   

admin.site.register(Team)
admin.site.register(Home_Away, Home_Away_Form)
admin.site.register(WinnerPick, WinnerPickForm)