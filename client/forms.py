from django import forms
from .models import Client
from psychologues.models import Psychologue


      
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'phone', 'email', 'categorie')
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('psy_user')
        
        super(ClientForm, self).__init__(*args, **kwargs)
        self.psychologue = Psychologue.objects.get(user = user)
        self.fields['categorie'].queryset = self.psychologue.clientele.all()
        # self.fields['categorie_probleme'].queryset = ServiceOffert.objects.none()

        