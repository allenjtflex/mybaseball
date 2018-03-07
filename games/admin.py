from django.contrib import admin
from .models import Member,Team,Cup, CupGroup,BatResult,Schedule
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ( 'team_title', 'is_active' )
    list_display_links = (  'team_title', )
    list_per_page = 10
    #search_fields = ['title']

admin.site.register(Member)
admin.site.register(Team,TeamAdmin)
admin.site.register(Cup)


class CupGroupAdmin(admin.ModelAdmin):
    list_display = ( 'cup', 'group','team' )
    list_display_links = (  'cup','team', )
    list_per_page = 10
    #search_fields = ['title']

admin.site.register(CupGroup,CupGroupAdmin)



class BatResultAdmin(admin.ModelAdmin):
    list_display = ( 'catcode', 'description','batseats','batcount' )
    list_display_links = (  'catcode','description', )
    list_per_page = 10
    #search_fields = ['tit
admin.site.register(BatResult,BatResultAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ( 'dif_date', 'cup','guest' ,'home','playdate')
    list_display_links = (  'cup','playdate', )
    list_per_page = 10
admin.site.register(Schedule,ScheduleAdmin)
