from django.db import models
class  worker_company(models.Model):
    name= models.CharField(max_length=100)
    bio=models.CharField(max_length=1024)
    def __str__(self):
        return self.name
    
class Worker(models.Model):
    company=models.ForeignKey(worker_company, on_delete=models.SET_NULL , null=True )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    medical_history = models.TextField()
    safety_breaches = models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
