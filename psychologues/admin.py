from django.contrib import admin
from .models import SecteurDePratique, Mandat, Langue, Orientation, Psychologue, Intervention, Competence, ServiceOffert
# Register your models here.
admin.site.register(SecteurDePratique)
admin.site.register(Mandat)
admin.site.register(Langue)
admin.site.register(Orientation)
admin.site.register(Psychologue)
admin.site.register(Intervention)
admin.site.register(Competence)
admin.site.register(ServiceOffert)