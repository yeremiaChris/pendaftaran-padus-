from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class PesertaForm(ModelForm):
    class Meta:
        model = Peserta
        fields = '__all__'
        exclude = ['foto']
class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'

class JadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'

class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        