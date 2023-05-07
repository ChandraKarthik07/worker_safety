from rest_framework import serializers 
from .models import Worker,worker_company

class WorkercompanySerializer(serializers.ModelSerializer):
    Worker_count=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = worker_company
        fields = '__all__'
    def get_Worker_count(self,obj):
        count= obj.worker_set.count()
        return count
        
class WorkerSerializer(serializers.ModelSerializer):
    company = WorkercompanySerializer()
    class Meta:
        model = Worker
        fields = '__all__'

