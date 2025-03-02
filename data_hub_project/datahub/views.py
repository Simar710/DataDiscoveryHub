# datahub/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Dataset
from rest_framework import generics
from .serializers import DatasetSerializer

class DatasetListView(ListView):
    model = Dataset
    template_name = 'datahub/dataset_list.html'
    context_object_name = 'datasets'

class DatasetCreateView(CreateView):
    model = Dataset
    template_name = 'datahub/dataset_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('dataset-list')

class DatasetListAPI(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer