from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    medical_history = models.TextField()
    safety_breaches = models.IntegerField(default=0)

    def __str__(self):
        return self.name
