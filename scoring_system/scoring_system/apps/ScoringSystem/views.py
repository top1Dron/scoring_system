from django.shortcuts import *
from django.template import RequestContext
from django.template.loader import render_to_string
from .forms import Bajana_suma_credituForm, DohidForm, VikForm, Family_stanForm, DitiForm, OsvitaForm, PosadaForm, Sfera_robotiForm, StatForm, ClientForm
from .models import Client, Anketa, Stat, Family_stan, Vik, Sfera_roboti, Diti, Osvita, Posada, Dohid, Bajana_suma_creditu
from .services import Services
import json

services = Services()

def index(request):
    return render(request, 'ScoringSystem/index.html', {'form_number': 1 })


def start_quiz(request, pk=1, *args, **kwargs):
    if pk == 1:
        if request.method == 'POST':
            form = Bajana_suma_credituForm(data=request.POST)
            if form.is_valid():
                services.answerDict['loan_amount'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': DohidForm,
                'form_number': 2,
            }, RequestContext(request))
        else:
            return render(request, 'ScoringSystem/question_form.html', {
                'form': Bajana_suma_credituForm(),
                'form_number': 1,
        }, RequestContext(request))
    elif pk == 2:
        if request.method == 'POST':
            form = DohidForm(data=request.POST)
            if form.is_valid():
                services.answerDict['earnings'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': VikForm,
                'form_number': 3,
            }, RequestContext(request))
    elif pk == 3:
        if request.method == 'POST':
            form = VikForm(data=request.POST)
            if form.is_valid():
                services.answerDict['age'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': Family_stanForm,
                'form_number': 4,
            }, RequestContext(request))
    elif pk == 4:
        if request.method == 'POST':
            form = Family_stanForm(data=request.POST)
            if form.is_valid():
                services.answerDict['family_status'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': DitiForm,
                'form_number': 5,
            }, RequestContext(request))
    elif pk == 5:
        if request.method == 'POST':
            form = DitiForm(data=request.POST)
            if form.is_valid():
                services.answerDict['children_count'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': OsvitaForm,
                'form_number': 6,
            }, RequestContext(request))
    elif pk == 6:
        if request.method == 'POST':
            form = OsvitaForm(data=request.POST)
            if form.is_valid():
                services.answerDict['education'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': PosadaForm,
                'form_number': 7,
            }, RequestContext(request))
    elif pk == 7:
        if request.method == 'POST':
            form = PosadaForm(data=request.POST)
            if form.is_valid():
                services.answerDict['position'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': Sfera_robotiForm,
                'form_number': 8,
            }, RequestContext(request))
    elif pk == 8:
        if request.method == 'POST':
            form = Sfera_robotiForm(data=request.POST)
            if form.is_valid():
                services.answerDict['sfera'] = request.POST["answer"]
            return render(request, 'ScoringSystem/question_form.html', {
                'form': StatForm,
                'form_number': 9,
            }, RequestContext(request))
    elif pk == 9:
        if request.method == 'POST':
            form = StatForm(data=request.POST)
            if form.is_valid():
                services.answerDict['sex'] = request.POST["answer"]
            return render(request, 'ScoringSystem/client_form.html', {
                'form': ClientForm,
                'form_number': 10,
            }, RequestContext(request))
    elif pk == 10:
        if request.method == 'POST':

            #TODO make data saving and render the last page
            newClient = Client.objects.create(
                Name_cl = request.POST['name'],
                Surname_cl = request.POST['surname'],
                Po_batk_cl = request.POST['secondName'],
                Seria_passport = request.POST['passportSerial'],
                Nomer_passport = request.POST['passportNumber'],
            )

            newAnketa = Anketa.objects.create(
                Code_Stati_id = services.answerDict['sex'],
                Code_Stanu_id = services.answerDict['family_status'],
                Code_Sferi_id = services.answerDict['sfera'],
                Code_Viku_id = services.answerDict['age'],
                Code_ditey_id = services.answerDict['children_count'],
                Code_osvity_id = services.answerDict['education'],
                Code_Posadi_id = services.answerDict['position'],
                Code_Dohodu_id = services.answerDict['earnings'],
                Code_bajanoi_sumi_id = services.answerDict['loan_amount'],
                Kod_clienta = newClient,
            )

            total_points = 0.0
            total_points += Vik.objects.get(id=services.answerDict['age']).Bal_viku
            total_points += Stat.objects.get(id=services.answerDict['sex']).Bal_stati
            total_points += Family_stan.objects.get(id=services.answerDict['family_status']).Bal_stanu
            total_points += Sfera_roboti.objects.get(id=services.answerDict['sfera']).Bal_sferi
            total_points += Diti.objects.get(id=services.answerDict['children_count']).Bal_ditey
            total_points += Osvita.objects.get(id=services.answerDict['education']).Bal_osviti
            total_points += Posada.objects.get(id=services.answerDict['position']).Bal_posadi
            total_points += Dohid.objects.get(id=services.answerDict['earnings']).Bal_dohodu

            loanAmountPoints = Bajana_suma_creditu.objects.get(id=services.answerDict['loan_amount']).Bal_sumi

            # with open('file.txt', 'w', encoding='utf-8') as f:
            #     print(f'vik {services.answerDict["age"]} {Vik.objects.get(id=services.answerDict["age"]).Bal_viku}', file=f)
            #     print(f'stat {services.answerDict["sex"]} {Stat.objects.get(id=services.answerDict["sex"]).Bal_stati}', file=f)
            #     print(f'family_stan {services.answerDict["family_status"]} {Family_stan.objects.get(id=services.answerDict["family_status"]).Bal_stanu}', file=f)
            #     print(f'Sfera_roboti {services.answerDict["sfera"]} {Sfera_roboti.objects.get(id=services.answerDict["sfera"]).Bal_sferi}', file=f)
            #     print(f'Diti {services.answerDict["children_count"]} {Diti.objects.get(id=services.answerDict["children_count"]).Bal_ditey}', file=f)
            #     print(f'Osvita {services.answerDict["education"]} {Osvita.objects.get(id=services.answerDict["education"]).Bal_osviti}', file=f)
            #     print(f'Posada {services.answerDict["position"]} {Posada.objects.get(id=services.answerDict["position"]).Bal_posadi}', file=f)
            #     print(f'Dohid {services.answerDict["earnings"]} {Dohid.objects.get(id=services.answerDict["earnings"]).Bal_dohodu}', file=f)
            #     print(f'total: {total_points}', file=f)
            #     print(f'Bajana_suma_creditu {services.answerDict["loan_amount"]} {Bajana_suma_creditu.objects.get(id=services.answerDict["loan_amount"]).Bal_sumi} {loanAmountPoints}', file=f)

            return render(request, 'ScoringSystem/result_form.html', {
                'total_points': round(total_points * 100, 2),
                'loan_amount_points': round(loanAmountPoints * 100, 2),
            }, RequestContext(request))