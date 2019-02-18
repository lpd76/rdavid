from django.shortcuts import render, get_list_or_404
from psychologues.models import Psychologue, ServiceOffert
from .models import SectionText

# Create your views here.
def index(request):
    psychologues = get_list_or_404(Psychologue)
    sectiontext= get_list_or_404(SectionText)
    #services_offerts = get_list_or_404(ServiceOffert)
    
    def get_besoins_as_list(ServiceOffert):
        services_offerts = ServiceOffert.objects.all()
        # on va chercher les types (distinct) de clientele qui sont déservie
        type_de_clientele_deservie = services_offerts.order_by().values('clientele__categorie_clientele__id','clientele__categorie_clientele__nom_fr').distinct()
        # pour chacune des clientele déservie
        clientele_list = []
        for clientele in type_de_clientele_deservie:
            clientele_name = clientele['clientele__categorie_clientele__nom_fr']
            clientele_list.append(clientele_name)
            # on va chercher les catégorie de probleme qui les affligent
            categorie_de_probleme = services_offerts.filter(clientele__categorie_clientele__nom_fr = clientele_name).order_by().values('clientele__probleme__categorie__id', 'clientele__probleme__categorie__nom_fr').distinct()
            category=[]
            for categorie in categorie_de_probleme:
                cat_name = categorie['clientele__probleme__categorie__nom_fr']
                category.append(cat_name)
                # on va chercher les problemes appartement a ce type
                problemes = services_offerts.filter(clientele__categorie_clientele__nom_fr = clientele_name,\
                                                    clientele__probleme__categorie__nom_fr = cat_name).order_by().values('clientele__probleme__id', 'clientele__probleme__nom_fr').distinct()
                probleme_list= []
                for probleme in problemes:
                    probleme_list.append(probleme['clientele__probleme__nom_fr'])
                category.append(probleme_list)
            clientele_list.append(category)
        return clientele_list
    
    def get_besoins_as_dict(ServiceOffert):
        all_services = ServiceOffert.objects.all()
    # on va chercher les types (distinct) de clientele qui sont déservie
        type_de_clientele_deservie = all_services.order_by().values('clientele__categorie_clientele__id','clientele__categorie_clientele__nom_fr').distinct()
        # pour chacune des clientele déservie
        clientele_problemes = {}
        for clientele in type_de_clientele_deservie:
            # print(clientele['clientele__categorie_clientele__id'], clientele['clientele__categorie_clientele__nom_fr'])
            clientele_name = clientele['clientele__categorie_clientele__nom_fr']
            # on va chercher les catégorie de probleme qui les affligent
            categorie_de_probleme = all_services.filter(clientele__categorie_clientele__nom_fr=clientele['clientele__categorie_clientele__nom_fr']).order_by().values('clientele__probleme__categorie__id', 'clientele__probleme__categorie__nom_fr').distinct()
            problems_by_category={}
            for categorie in categorie_de_probleme:
                # print(3*"-", categorie['clientele__probleme__categorie__id'], categorie['clientele__probleme__categorie__nom_fr'])
                cat_name = categorie['clientele__probleme__categorie__nom_fr']
                # on va chercher les problemes appartement a ce type
                problemes = all_services.filter(clientele__categorie_clientele__nom_fr=clientele['clientele__categorie_clientele__nom_fr'],\
                                               clientele__probleme__categorie__nom_fr=categorie['clientele__probleme__categorie__nom_fr']).order_by().values('clientele__probleme__id', 'clientele__probleme__nom_fr').distinct()
                probleme_list= []
                for probleme in problemes:
                    # service_obj = all_services.filter(clientele__categorie_clientele__id = clientele['clientele__categorie_clientele__id'],\
                    #                  clientele__probleme__categorie__id = categorie['clientele__probleme__categorie__id'],\
                    #                  clientele__probleme__id = probleme['clientele__probleme__id'])
                    # print(5*"--",probleme['clientele__probleme__id'], probleme['clientele__probleme__nom_fr'], service_obj)
                    probleme_list.append(probleme['clientele__probleme__nom_fr'])
                problems_by_category[cat_name] = probleme_list
            clientele_problemes[clientele_name] = problems_by_category
        return clientele_problemes
    
    context = {'staff':psychologues, 'sectiontext':sectiontext, 'services_offerts_list':get_besoins_as_list(ServiceOffert),\
               'services_offerts_dict':get_besoins_as_dict(ServiceOffert)}
    return render(request, 'index/index.html', context)
    