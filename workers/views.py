from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Worker,worker_company
from .serializers import WorkerSerializer,WorkercompanySerializer
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
    
class create_worker(APIView):
    def get_object(self,pk):
        try:
            return Worker.objects.get(name=pk)
        except Worker.DoesNotExist:
            raise Http404
         
            
    def get(self,request,pk):
        workers=self.get_object(pk)
        serializer = WorkerSerializer(workers)
        return Response(serializer.data)
    def put(self,request,pk):
        workers=self.get_object(pk)
        # workers.update(name=request.data['name'],age=request.data['age'],address=request.data['address'],contact_info=request.data['contact_info'],medical_history=request.data['medical_history'],safety_breaches=request.data['safety_breaches'])
        # workers.save()
        serializer=WorkerSerializer(workers,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        workers=self.get_object(pk)
        workers.delete()
        return Response('worker was deleted')
    
    
    
# @api_view(['GET','PUT','DELETE'])
# def create_worker(request,pk):
#     workers=Worker.objects.get(name=pk)
#     if request.method=='GET':
#         serializer = WorkerSerializer(workers)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         workers.update(name=request.data['name'],age=request.data['age'],address=request.data['address'],contact_info=request.data['contact_info'],medical_history=request.data['medical_history'],safety_breaches=request.data['safety_breaches'])
#         workers.save()
        
#         serializer=WorkerSerializer(workers,many=True)
#         return Response(serializer.data)
#     if request.method=="DELETE":
#         workers.delete()
#         return Response('worker was deleted')
#     return Response()
def worker_data(request):
    
    return render(request, 'workers/index.html')
class company(APIView):
    def get(self,request):
        company=worker_company.objects.all()
        serializer=WorkercompanySerializer(company,many=True)
        return Response(serializer.data)