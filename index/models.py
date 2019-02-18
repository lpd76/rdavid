from django.db import models

# Create your models here.
class SectionText(models.Model):
    nom_fr = models.CharField(max_length = 200, unique=True)
    nom_en = models.CharField(max_length = 200, blank=True)
    text_fr = models.TextField(max_length = 1000, blank=True)
    text_an = models.TextField(max_length = 1000, blank=True)
    
    def __str__(self):
        return self.nom_fr