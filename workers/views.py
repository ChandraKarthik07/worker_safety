from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Worker
from .serializers import WorkerSerializer
from django.shortcuts import render
@api_view(['GET','POST'])
def worker_list(request):
    if request.method=='GET':
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        workers=Worker.objects.create(name=request.data['name'],age=request.data['age'],address=request.data['address'],contact_info=request.data['contact_info'],medical_history=request.data['medical_history'],safety_breaches=request.data['safety_breaches'])
        workers.save()
        serializer=WorkerSerializer(workers,many=False)
        return Response(serializer.data)
@api_view(['GET','PUT','DELETE'])
def create_worker(request,pk):
    workers=Worker.objects.get(name=pk)
    if request.method=='GET':
        serializer = WorkerSerializer(workers)
        return Response(serializer.data)
    if request.method=='PUT':
        workers.update(name=request.data['name'],age=request.data['age'],address=request.data['address'],contact_info=request.data['contact_info'],medical_history=request.data['medical_history'],safety_breaches=request.data['safety_breaches'])
        workers.save()
        
        serializer=WorkerSerializer(workers,many=True)
        return Response(serializer.data)
    if request.method=="DELETE":
        workers.delete()
        return Response('worker was deleted')
    return Response()
def worker_data(request):
    
    return render(request, 'workers/index.html')