from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer

class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
def worker_data(request):
    return render(request, 'workers/index.html')