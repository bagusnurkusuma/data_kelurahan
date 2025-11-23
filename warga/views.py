from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm,PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView 
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework import viewsets # Impor viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'
    ordering = ['-tanggal_lapor']

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('id')
    serializer_class = WargaSerializer

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('id')
    serializer_class = PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

    # Override get_permissions agar POST bisa tanpa login
    def get_permissions(self):
        if self.action == 'create':  # jika method POST
            return [AllowAny()]  # izinkan semua user
        return [IsAuthenticatedOrReadOnly()]  # metode lain tetap pakai permission default

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('judul')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']