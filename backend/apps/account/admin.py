from django.contrib import admin

from .models import Departament, Account, Wallet, Achievement, Position


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass