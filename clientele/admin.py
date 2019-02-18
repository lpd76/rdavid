from django.contrib import admin
from .models import CategorieProbleme, Probleme, Clientele, CategorieClientele

# Register your models here.
admin.site.register(CategorieProbleme)
admin.site.register(Probleme)
admin.site.register(Clientele)
admin.site.register(CategorieClientele)