from django.shortcuts import render,redirect
from .models import *
from .forms import PesertaForm,AgendaForm,JadwalForm,CreationUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def agenda(request):
    agenda = Agenda.objects.all()
    context = {
        'agenda': agenda
    }
    return render(request,'account/agenda.html',context)

@login_required(login_url='login')
def dashboard(request):
    peserta = Peserta.objects.all()
    context = {
        'peserta': peserta
    }
    return render(request,'account/sidebar.html',context)

@login_required(login_url='login')
def jadwal(request):
    jadwal = Jadwal.objects.all()
    context = {
        'jadwal': jadwal
    }
    return render(request,'account/jadwal.html',context)

@login_required(login_url='login')
def beranda(request):
    jumlah_peserta = Peserta.objects.all().count()
    jumlah_jadwal = Jadwal.objects.all().count()
    jumlah_agenda = Agenda.objects.all().count()
    context = {
        'jumlah_peserta':jumlah_peserta,
        'jumlah_jadwal': jumlah_jadwal,
        'jumlah_agenda': jumlah_agenda,
    }
    return render(request,'account/beranda.html',context)

def createPeserta(request):
    form = PesertaForm()
    if request.method == 'POST':
        form = PesertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utama')
    context = {
        'form': form
    }
    return render(request,'account/create_peserta.html',context)
@login_required(login_url='login')
def updatePeserta(request,pk):
    peserta = Peserta.objects.get(id_peserta=pk)
    form = PesertaForm(instance=peserta)
    if request.method == 'POST':
        form = PesertaForm(request.POST,instance=peserta)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request,'account/peserta_form.html',context)
@login_required(login_url='login')
def deletePeserta(request,pk):
    peserta = Peserta.objects.get(id_peserta=pk)
    if request.method == 'POST':
        peserta.delete()
        return redirect('dashboard')
    context = {
        'peserta':peserta
    }
    return render(request,'account/delete_peserta.html',context)

@login_required(login_url='login')
def createAgenda(request):
    form =AgendaForm()
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beranda')

    context = {
        'form': form
    }
    return render(request,'account/agenda_form.html',context)

@login_required(login_url='login')
def updateAgenda(request,pk):
    agenda = Agenda.objects.get(id_agenda=pk)
    form = AgendaForm(instance=agenda)
    if request.method == 'POST':
        form = AgendaForm(request.POST,instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('agenda')
    context = {
        'form': form
    }
    return render(request,'account/agenda_form.html',context)

@login_required(login_url='login')
def deleteAgenda(request,pk):
    agenda = Agenda.objects.get(id_agenda=pk)
    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda')
    context = {
        'agenda': agenda
    }
    return render(request,'account/delete_agenda.html',context)

@login_required(login_url='login')
def createJadwal(request):
    form  = JadwalForm()
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beranda')
    context = {
        'form': form
    }
    return render(request,'account/jadwal_form.html',context)

@login_required(login_url='login')
def updateJadwal(request,pk):
    jadwal = Jadwal.objects.get(id_jadwal=pk)
    form = JadwalForm(instance=jadwal)
    if request.method == 'POST':
        form = JadwalForm(request.POST,instance=jadwal)
        if form.is_valid():
            form.save()
            return redirect('jadwal')
    context = {
        'form': form
    }
    return render(request,'account/jadwal_form.html',context)

@login_required(login_url='login')
def deleteJadwal(request,pk):
    jadwal = Jadwal.objects.get(id_jadwal=pk)
    if request.method == 'POST':
        jadwal.delete()
        return redirect('jadwal')
    context = {
        'jadwal': jadwal
    }
    return render(request,'account/delete_jadwal.html',context)


def loginpage(request):

    if request.method == 'POST':
        # username dan password itu nama dari input template
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('beranda')
        else:
            messages.info(request,'ada yang salah cuy')
    return render(request,'account/login.html')

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreationUserForm()
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context  = {
        'form': form
    }
    return render(request,'account/register.html',context)

def utama(request):
    return render(request,'account/indeks.html')
def jadwalUtama(request):
    agenda = Agenda.objects.all()
    jadwal = Jadwal.objects.all()
    context = {
        'agenda': agenda,
        'jadwal': jadwal
    }
    return render(request,'account/jadwal_utama.html',context)