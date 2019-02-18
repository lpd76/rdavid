from django.db import models
from django.contrib.auth.models import User
from clientele.models import Clientele, CategorieClientele
from django.urls import reverse


# Create your models here.
class SecteurDePratique(models.Model):
    nom_fr = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom_fr
    class Meta:
        ordering = ['nom_fr']
    
class Mandat(models.Model):
    nom_fr = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom_fr
    class Meta:
        ordering = ['nom_fr']
        
class Langue(models.Model):
    nom_fr = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom_fr
    class Meta:
        ordering = ['nom_fr']
class Orientation(models.Model):
    nom_fr = models.CharField(max_length=200, unique=True)
    non_en = models.CharField(max_length=200, blank=True)
    desc_fr = models.TextField(max_length=1000, blank=True)
    desc_ang = models.TextField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.nom_fr
    class Meta:
        verbose_name_plural = 'Orientations'
        ordering = ['nom_fr']
class Intervention(models.Model):
    nom_fr = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom_fr
    class Meta:
        ordering = ['nom_fr']
    
class Psychologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permis_num = models.IntegerField(blank=True)
    permis_date = models.DateField(blank=True, default='2018-01-01')
    avatar = models.ImageField(upload_to = 'psy_avatar/')
    phone = models.CharField(max_length=10, blank=True)
    fax = models.CharField(max_length=10, blank=True)
    bio = models.TextField(max_length=1700, blank=True)
    education = models.CharField(max_length=70, blank=True)
    site_web = models.URLField(blank=True)
    linked_in = models.URLField(blank=True)
    orientation = models.ManyToManyField(Orientation)
    secteur_de_pratique = models.ManyToManyField(SecteurDePratique)
    mandat = models.ManyToManyField(Mandat, blank = True)
    clientele = models.ManyToManyField(CategorieClientele, blank=True)
    langue = models.ManyToManyField(Langue)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    class Meta:
        ordering = ['user']
        
    def get_absolute_url(self):
        return reverse('psychologues_profile', args=[str(self.id)])
    def get_home_url(self):
        return reverse('psychologues_home', args=[str(self.id)])
        
class Competence(models.Model):
    psychologue = models.ForeignKey(Psychologue, on_delete=models.CASCADE)
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
    # orientation peut etre nul et ca cause des probleme a l'affichage
        try:
            return_str =  self.psychologue.user.first_name +" "+ self.psychologue.user.last_name +" "+ self.intervention.nom_fr +" "+self.orientation.nom_fr
        except:
            return_str =  self.psychologue.user.first_name +" "+ self.psychologue.user.last_name +" "+ self.intervention.nom_fr  
        return return_str
    class Meta:
        ordering = ['psychologue', 'intervention', 'orientation']
        
class ServiceOffert(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    clientele = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    
    def __str__(self):
        return  self.competence.psychologue.user.first_name + " " + \
            self.competence.psychologue.user.last_name + " " + \
            self.competence.intervention.nom_fr + " " + \
            self.clientele.categorie_clientele.nom_fr + " " + \
            self.clientele.probleme.nom_fr
    