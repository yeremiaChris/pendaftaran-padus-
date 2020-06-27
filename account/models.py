from django.db import models
from datetime import datetime


# Create your models here. 
class Peserta(models.Model):
    id_peserta = models.CharField(max_length=6,unique=True,primary_key=True)
    tgl_daftar = models.DateTimeField(default=datetime.now)
    nama = models.CharField(max_length=10)
    email = models.EmailField()
    tmp_lahir = models.CharField(max_length=10)
    tgl_lahir = models.DateTimeField(default=datetime.now)
    jenjang = models.CharField(max_length=3)
    no_telp = models.CharField(max_length=15)
    alamat = models.CharField(max_length=10)
    jadwal_1 = models.CharField(max_length=15)
    jadwal_2 = models.CharField(max_length=15)
    status = models.CharField(max_length=50)
    foto = models.ImageField(default='default.jpg',upload_to='gambar')
    def __str__(self):
        return self.id_peserta

class Jadwal(models.Model):
    id_jadwal = models.CharField(max_length=2,unique=True,primary_key=True)
    hari_waktu = models.DateTimeField(default=datetime.now)
    tempat = models.CharField(max_length=10)
    
    def __str__(self):
        return self.id_jadwal

class Agenda(models.Model):
    id_agenda = models.CharField(max_length=6,unique=True,primary_key=True)
    hari_waktu = models.DateTimeField(default=datetime.now)
    agenda = models.CharField(max_length=15)
    tempat = models.CharField(max_length=7)

    def __str__(self):
        return self.id_agenda
    

