from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,pagination,viewsets
from django.http import Http404
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from .models import Worker,worker_company
from .serializers import WorkerSerializer,WorkercompanySerializer
from django.shortcuts import render ,get_object_or_404
# @api_view(['GET','POST'])
# def worker_list(request):
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAuthenticated]
#     if request.method=='GET':
#         workers = Worker.objects.all()
        
#         serializer = WorkerSerializer(workers, many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         workers=Worker.objects.create(name=request.data['name'],age=request.data['age'],address=request.data['address'],contact_info=request.data['contact_info'],medical_history=request.data['medical_history'],safety_breaches=request.data['safety_breaches'])
#         workers.save()
#         serializer=WorkerSerializer(workers,many=False)
#         return Response(serializer.data)

# class worker_list(APIView):
#     pagination_class = PageNumberPagination
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [AllowAny]

#     def post(self, request):
#         workers = Worker.objects.create(**request.data)
#         workers.save()
#         serializer = WorkerSerializer(workers, many=False)
#         return Response(serializer.data)

#     def get(self, request):
#         workers = Worker.objects.all()
#         paginator = self.pagination_class()
#         page = paginator.paginate_queryset(workers, request)
#         if page is not None:
#             serializer = WorkerSerializer(page, many=True)
#             return paginator.get_paginated_response(serializer.data)
#         serializer = WorkerSerializer(workers, many=True)
#         return Response(serializer.data)
class worker_list(viewsets.ModelViewSet):
    queryset=Worker.objects.all()
    serializer_class=WorkerSerializer
    def retrieve(self,request,pk=None):
        worker=get_object_or_404(self.queryset,name=pk)
        serializer=WorkerSerializer(worker)
        return Response(serializer.binddata)
    
# class create_worker(APIView):
    pagination_class = pagination.PageNumberPagination
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get_object(self,pk):
        try:
            return Worker.objects.get(name=pk)
        except Worker.DoesNotExist:
            raise Http404    
    def get(self,request,pk):
        workers=self.get_object(pk)
        paginator=self.pagination_class()
        page =paginator.paginate_queryset(workers,request)
        if page is not None:
            serializer=WorkerSerializer(page,many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = WorkerSerializer(workers,many=True)
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