from django.contrib import admin
from .models import Anketa, Client, Bajana_suma_creditu, Diti, Dohid, Family_stan, Osvita, Posada, Sfera_roboti, Stat, Vik


@admin.register(Anketa)
class AnketaAdmin(admin.ModelAdmin):
    list_display = ('id','Code_Stati', 'Code_Stanu', 'Code_Sferi', 'Code_Viku', 'Code_ditey', 'Code_osvity', 'Code_Posadi', 'Code_Dohodu', 'Code_bajanoi_sumi', 'Kod_clienta')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','Name_cl','Surname_cl', 'Po_batk_cl', 'Seria_passport', 'Nomer_passport')


@admin.register(Osvita)
class OsvitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_osviti','Name_osviti')


@admin.register(Vik)
class VikAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_viku','Vik')


@admin.register(Posada)
class PosadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_posadi','Name_posadi')


@admin.register(Dohid)
class DohidAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_dohodu','Range_dohodu')


@admin.register(Diti)
class DitiAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_ditey','Kilkist_ditey')


@admin.register(Sfera_roboti)
class Sfera_robotiAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_sferi','Name_Sferi')


@admin.register(Family_stan)
class Family_stanAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_stanu','Name_stanu')


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_stati','Name_stati')


@admin.register(Bajana_suma_creditu)
class Bajana_suma_credituAdmin(admin.ModelAdmin):
    list_display = ('id', 'Bal_sumi','Znachennya_creditu')