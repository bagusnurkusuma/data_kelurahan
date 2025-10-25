from django import forms
from .models import Warga,Pengaduan


class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = [
            'nama_lengkap',
            'nik',
            'alamat',
            'no_telepon',
        ]

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = [
            'judul',
            'deskripsi',
            'status',
            'pelapor',
        ]