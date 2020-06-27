from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginpage,name='login'),
    path('logout/', views.logoutpage,name='logout'),
    path('register/', views.register,name='register'),
    path('', views.beranda,name='beranda'),
    path('utama', views.utama,name='utama'),
    path('jadwal_utama', views.jadwalUtama,name='jadwal-utama'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('agenda/', views.agenda,name='agenda'),
    path('jadwal/', views.jadwal,name='jadwal'),
    path('create_peserta/', views.createPeserta,name='create-peserta'),
    path('update_peserta/<str:pk>/', views.updatePeserta,name='update-peserta'),
    path('delete_peserta/<str:pk>/', views.deletePeserta,name='delete-peserta'),
    path('create_agenda/', views.createAgenda,name='create-agenda'),
    path('update_agenda/<str:pk>', views.updateAgenda,name='update-agenda'),
    path('delete_agenda/<str:pk>', views.deleteAgenda,name='delete-agenda'),
    path('create_jadwal/', views.createJadwal,name='create-jadwal'),
    path('update_jadwal/<str:pk>', views.updateJadwal,name='update-jadwal'),
    path('delete_jadwal/<str:pk>', views.deleteJadwal,name='delete-jadwal'),
]