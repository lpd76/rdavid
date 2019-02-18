from django.db import models

# Create your models here.
class CategorieProbleme(models.Model):
    nom_fr = models.CharField(max_length=200, unique=True)
    class Meta:
        ordering = ['nom_fr']
    def __str__(self):
        return self.nom_fr
    
class Probleme(models.Model):
    categorie = models.ForeignKey(CategorieProbleme, on_delete=models.CASCADE)
    nom_fr = models.CharField(max_length=200, unique=False)
    def __str__(self):
        return self.categorie.nom_fr + " : " + self.nom_fr
    class Meta:
        unique_together = ('categorie', 'nom_fr')
        ordering = ['categorie', 'nom_fr']
        
class CategorieClientele(models.Model):
    nom_fr = models.CharField(max_length=200, unique=False)
    class Meta:
        ordering = ['nom_fr']
    def __str__(self):
        return self.nom_fr 
    
class Clientele(models.Model):
    categorie_clientele = models.ForeignKey(CategorieClientele, on_delete=models.CASCADE)
    probleme = models.ForeignKey(Probleme, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('categorie_clientele', 'probleme')
        ordering = ['categorie_clientele', 'probleme']
    def __str__(self):
        return self.categorie_clientele.nom_fr + " : " + self.probleme.categorie.nom_fr + " : " + self.probleme.nom_fr
