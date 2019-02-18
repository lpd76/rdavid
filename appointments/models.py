from django.db import models
from client.models import Client
from psychologues.models import Intervention
from django.urls import reverse
# from django.urls import reverse

# Create your models here.
class Status(models.Model):
    nom_fr = models.CharField(max_length = 40)
    def __str__(self):
        return self.nom_fr
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE,)
    intervention = models.ForeignKey(Intervention, on_delete = models.SET_NULL, null=True)
    # created_on = models.DateField(auto_now_add=True)
    created_on = models.DateField()
    scheduled_on = models.DateTimeField()
    note = models.TextField(max_length = 2000, blank=True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL,  null=True)
    
    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])
    
    def get_update_url(self):
        return reverse('appointment_update', args=[str(self.id)])
    
    
    