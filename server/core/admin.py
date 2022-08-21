from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'groupr2', 'price', 'final_rating', 'dr')

class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('groupr2', 'canAccessFinalRatings', 'canSelectTeam')}),
    )

admin.site.register(User,MyUserAdmin)
admin.site.register(PlayerResponse)
admin.site.register(GroupR2)
admin.site.register(Team)
admin.site.register(Player, PlayerAdmin)