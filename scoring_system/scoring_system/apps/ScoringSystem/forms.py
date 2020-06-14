from django import forms
from django.forms.utils import ValidationError
from .models import Vik, Family_stan, Diti, Osvita, Posada, Sfera_roboti, Bajana_suma_creditu, Dohid, Stat, Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('Surname_cl', 'Name_cl', 'Po_batk_cl', 'Seria_passport', 'Nomer_passport')


class Bajana_suma_credituForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Bajana_suma_creditu.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='1. Бажана сума кредиту?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    def clean(self):
        answer = self.cleaned_data.get('answer')
        if not answer:
            raise forms.ValidationError("Будь ласка, виберіть хоча б один варіант")

        return self.cleaned_data


    class Meta:
        model = Bajana_suma_creditu
        fields = ()


class DohidForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Dohid.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='2. Ваш дохід?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Dohid
        fields = ()


class VikForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Vik.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='3. Який ваш вік?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Vik
        fields = ()


class Family_stanForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Family_stan.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='4. Ваш сімейний статус?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Family_stan
        fields = ()


class DitiForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Diti.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='5. У вас є діти?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Diti
        fields = ()


class OsvitaForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Osvita.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='6. Чи є у вас освіта?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Osvita
        fields = ()


class PosadaForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Posada.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='7. Яка у вас посада?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Posada
        fields = ()


class Sfera_robotiForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Sfera_roboti.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='8. Яке Ваше місце роботи?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Sfera_roboti
        fields = ()


class StatForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Stat.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None,
        label='9. Ваша стать?',
        error_messages={'required': 'Будь ласка, виберіть хоча б один варіант'}
    )


    class Meta:
        model = Stat
        fields = ()