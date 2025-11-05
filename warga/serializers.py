from rest_framework import serializers
from .models import Warga,Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal_registrasi']

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = ['id','judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor']