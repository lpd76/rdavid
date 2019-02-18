import uuid
from django.db import models
from psychologues.models import Psychologue
from clientele.models import CategorieClientele
from django.urls import reverse


# Create your models here.
class Status(models.Model):
    nom_fr = models.CharField(max_length = 20)
    class Meta:
        ordering = ['nom_fr']
    def __str__(self):
        return self.nom_fr


class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    categorie = models.ForeignKey(CategorieClientele, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=10, blank=True)
    # email = models.EmailField(blank=True)
    email = models.EmailField(unique=True)
    psychologue = models.ForeignKey(Psychologue, on_delete=models.SET_NULL, null=True)
    # created_on = models.DateField(auto_now_add=True)
    created_on = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
        
    def __str__(self):
        return self.nom + " " + self.prenom + " " + str(self.created_on) + " " + self.status.nom_fr
    
    class Meta:
        ordering = ['nom', 'prenom']
        
    def get_absolute_url(self):
        return reverse('client_view', args=[str(self.uuid)])