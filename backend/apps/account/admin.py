from django.contrib import admin

from .models import Account, Achievement, Position


@admin.register(Account)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
